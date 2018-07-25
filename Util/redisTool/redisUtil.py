# coding=utf-8

from ..commonTool import *
import redis
from rediscluster import StrictRedisCluster
from rediscluster.connection import ClusterConnectionPool


class RedisUtil(object):
    '''redis方法封装，支持redis及redis cluster'''
    pools = {}

    def __init__(self):
        pass

    @classmethod
    def getCon(cls, confSection, confFile='/config/test.yml'):
        """从redis的连接池中获取一个redis连接，如果没有则创建一个连接池
            :param confSection: 配置的section名
            :type confSection: string
            """
        try:
            key = confSection
            type = ConfigUtil.get(confSection, 'Type', confFile)
            if key not in cls.pools:
                server = ConfigUtil.get(confSection, 'Server', confFile)
                if type == 'Redis':
                    host, port, db = server.split(':')
                    pool = redis.ConnectionPool(host=host, port=port, db=db)
                elif type == 'Redis_Cluster':
                    startup_nodes = map(lambda s: {"host": s.split(':')[0], "port": s.split(':')[1]}, server.split(','))
                    pool = ClusterConnectionPool(startup_nodes=startup_nodes)
                cls.pools[key] = pool
            else:
                pass

            pool = cls.pools[key]
            if type == 'Redis':
                r = redis.Redis(connection_pool=pool)
            elif type == 'Redis_Cluster':
                r = StrictRedisCluster(connection_pool=pool, decode_responses=True)
            return r
        except Exception as e:
            print e

    @classmethod
    def execute(cls, command, key, *args, **kwargs):
        """执行redis命令
            :param command: 使用的redis命令
            :type command: string
            :param key: 执行命令的redis的key，需要替换的参数用%s表示
            :type key: string
            :param *args: 任意传入参数，开头的数值会与key中的%s匹配
            :type *args: 直接输入值
            :param **kwargs: 任意传入参数，如果包含confSection，会作为需要连接的redis地址，需要在config中添加对应的section
            :type **kwargs: 直接输入值，需要写成key = value的形式
            """
        try:
            # 判断是否传入confSection及confFile
            if "confSection" in kwargs and "confFile" in kwargs:
                r = cls.getCon(kwargs["confSection"], kwargs["confFile"])
                del kwargs["confSection"]
                del kwargs["confFile"]
            elif "confSection" in kwargs:
                r = cls.getCon(kwargs["confSection"])
                del kwargs["confSection"]
            elif "confFile" in kwargs:
                r = cls.getCon("Redis", kwargs["confFile"])
                del kwargs["confFile"]
            else:
                r = cls.getCon("Redis")

            s_count = key.count("%s")
            if s_count != 0:
                key_result = key % args[0:s_count]
                args_new = args[s_count:]
                return getattr(r, command)(key_result, *args_new, **kwargs)
            else:
                return getattr(r, command)(key, *args, **kwargs)

        except Exception as e:
            print e
