#  作者 ：  cathy  时间 ：2019-12-10
# -*- coding:utf-8 -*-

import requests
from  cfg  import  g_vcode
import pprint
from robot.api import logger
class Schoolclasslib:
    url='http://ci.ytesting.com/api/3school/school_classes'
    def listClass(self,gradeid=None):
        if gradeid !=None:
            params={
                "vcode":g_vcode,
                "action":'list_classes_by_schoolgrade',
                "gradeid":int(gradeid)
            }
        else:
            params = {
                "vcode": g_vcode,
                "action": 'list_classes_by_schoolgrade',
            }
        r=requests.get(self.url,params=params)
        dictbody=r.json()
        pprint.pprint(dictbody,indent=2)
        return dictbody

    def addClass(self,grade,name,studentlimit):
        payload={
            "vcode":g_vcode,
            "action":"add",
            "grade":int(grade),
            "name":name,
            "studentlimit":int(studentlimit),
        }
        r=requests.post(self.url,data=payload)
        dictbody = r.json()
        pprint.pprint(dictbody, indent=2)
        return dictbody
    def modifyClass(self,classid,grade,name,studentlimit):

        payload = {
            'classid':classid,
            "vcode": "g_vcode",
            "action": "add",
            "grade": int(grade),
            "name": name,
            "studentlimit": int(studentlimit),
        }
        r=requests.put(self.url,data=payload)
        dictbody = r.json()
        pprint.pprint(dictbody, indent=2)
        return dictbody
    def deleteClass(self,classid):
        payload = {
            "vcode": g_vcode,
        }
        url=self.url+'/%s'% classid
        r = requests.delete(url,data=payload)
        dictbody = r.json()
        pprint.pprint(dictbody, indent=2)
        return dictbody
    def deleteAllclass(self):
        dictbody=self.listClass()
        # pprint.pprint(dictbody,indent=2)
        if dictbody['retlist']:
            for one in dictbody['retlist']:
                print('这是one',one)
                self.deleteClass(one['id'])
            # self.deleteClass(dictbody['retlist'][0]['id'])
        dictbody2=self.listClass()
        print('888777777',dictbody2)
        if  dictbody2['retlist'] !=[]:
                raise Exception('can not delete all the class')
    def classlist_should_contain(self,grade__name,id,invitecode,name,studentlimit):

        itme={

            'grade__name': grade__name,
            'id': id,
            'invitecode': invitecode,
            'name': name,
            'studentlimit': studentlimit,
            'studentnumber': 0,

            'teacherlist': []}
        print('这是item',itme)
        # print('8888888',self.listClass()['retlist'])
        print(itme in self.listClass()['retlist'])

        # if itme in self.listClass()['retlist']:
        #     logger.info('pass')
        # else:
        #     raise Exception('fail')



if __name__ == '__main__':
    SC=Schoolclasslib()
    # print(SC.listClass(1))

    print(SC.addClass(1,'4班',50))
    # print(SC.deleteClass(276511))
    # SC.classlist_should_contain('七年级',277067,'2770676342631','4班',80)

