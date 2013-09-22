# -*- coding: utf-8 -*-
class MyDataWrapper():
    def __init__(self, data):
        pass
    
    def getDownloadLink(url):
        import re
        from json import dumps
        match = re.search(r'http:\/\/(?:pan|yun).baidu.com\/share\/link\?shareid=(\d+)&uk=(\d+)',url)
        if(match):
            import urllib2
            id = match.group(1)
            uk = match.group(2)
            header = {
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'
            }
            request = urllib2.Request(url = url, headers = header)
            html_code = urllib2.urlopen(request).read()

            #"md5\":\"88296788f23f16396e05e75a037bac00\"
            md5_match = re.search(r'"md5\\":\\\"(.+?)\\"',html_code)

            _url,_id,_uk,_error,_link,_type,type_baidu ="url","id","uk","error","link","type","baidu"
            if(md5_match):
                md5 = md5_match.group(1)
                #dlink\\":.+?(http.+?88296788f23f16396e05e75a037bac00\?.+?sh=1)
                reg = 'dlink\\\\":.+?(http.+?' + md5 + '\?.+?sh=1)'
                print reg;
                match = re.search(reg,html_code,re.MULTILINE)
                if(match):
                    return dumps({
                            _url : url,
                            _id:id,
                            _uk:uk,
                            _error:False,
                            _link:match.group(1).replace("\\",""),
                            _type:type_baidu
                            },
                            skipkeys=True
                    )
                else:
                    return dumps({
                            _url:url,
                            _id:id,
                            _uk:uk,
                            _error:True,
                            _type:type_baidu
                            },
                            skipkeys=True
                        )
            else:
                return dumps({
                    _url : url,
                    _id:id,
                    _uk:uk,
                    _error:True,
                    _type:type_baidu
                    },
                    skipkeys=True
                )
        else:
            return dumps({
                    _url : url,
                    _id:id,
                    _uk:uk,
                    _error : True,
                    _type : type_baidu
                    },
                    skipkeys=True
                )
