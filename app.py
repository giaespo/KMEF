#!/usr/bin/python3

from app.core.request import Request
from app.core.url import Urls
from app.core.plugin.softpersistent import SoftPersistence
from app.rootview import getRoot

from app.usersview import isServiceActive,setService,getDomains,setLanguage,getLogin,getLogout,isValidSession,getAllRights,getUserRights,isRightEnabled,getMailCounts,getAllUsers,getAllGroups,getAllOffices,getLoginHtml,getHomeHtml,index,runsub,getHomeHtmlLogin,autoLogin
from app.documentview import getArchives,getDocumentTypes,getDocumentType,getDocumentjson,printDocument,scanDocument,getCardvisibility,getArchiveHtml,getScan,acquire,getListIndex,getListAdditives,insertListItem,acquireMasterDoc,deleteFile,checkStatus,checkFile,saveFile,showAllCardFiles,acquireAttachment,getScanAttachments,\
showAllCardFiles,Cards,CardsSearch,getCard,getMailCards,getCardIndexes,setCardIndexes,getCardAdditives,setCardAdditives,getAcquisizione,getAttachments,getAttachment,attachDocument,removeAttachment,importDocument,insertCard,getRiepilogo,getSearchCards,getSearchCardsResult,getIndexesDetail,saveIndexesData,cardMenu,modifyIndexes,getAdditivesDetail,modifyAdditives,saveAdditivesData,signAdditive,\
sendCard,getPrint,saveDocument,getScanAttachmentsSearch,attachDocumentjson

from app.workflowview import getActivitiesToDo,getActivitiesInCharge,takeInCharge,forward,refuse,getActivity,activityToDo,activityInCharge

from app.core.views import get404
import http.cookies
import sys
import os
#import mfp
#import mfp.job
#import mfp.device

cookie=http.cookies.SimpleCookie()
#Verify Cookies existence
try:
    cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
except (Exception) as e:
    pass
#insert cookies in singleton 
p=SoftPersistence()
p.setCookie(cookie)
        

#get all post data
postdata=sys.stdin.read()
env=os.environ
env['POST']=postdata
#create request passing a dict with all post, get and json data
req=Request(env)

#create Dispatcher passing the request
urls=Urls(req)

#the url of application, use this with app.py?page=x
newUrls={
         'root':index,#getRoot,
         'run':runsub,
         'index':index,
         'language':setLanguage,
         'isServiceActive':isServiceActive,
         'setService':setService,
         'getDomains':getDomains,
         'login':getLogin,
         'loginhtml':getLoginHtml,
         'autoLogin':autoLogin,
         'isValidSession':isValidSession,
         'allRights':getAllRights,
         'userRights':getUserRights,
         'getAllUsers':getAllUsers,
         'getAllGroups':getAllGroups,
         'getAllOffices':getAllOffices,
         'isRightEnabled':isRightEnabled,
         'getMailCounts':getMailCounts,
         'logout':getLogout,
         'getHomeHtml':getHomeHtml,
         'getHomeHtmlLogin':getHomeHtmlLogin,
         
         #document calls
         'getAcquisizione':getAcquisizione,
         'getArchives':getArchives,
         'getDocumentTypes':getDocumentTypes,
         'getDocumentType':getDocumentType,
         'document':getDocumentjson,
         'getCardVisibility':getCardvisibility,
         'getArchiveHtml':getArchiveHtml,
         'listIndex':getListIndex,
         'listAdditives':getListAdditives,
         'getCards':Cards,
         'searchCards':CardsSearch,
         'getCard':getCard,
         'getMailCards':getMailCards,
         'getCardIndexes':getCardIndexes,
         'setCardIndexes':setCardIndexes,
         'getCardAdditives':getCardAdditives,
         'setCardAdditives':setCardAdditives,
         
         
         #insertCard
         'getAttachments':getAttachments,
         'getAttachment':getAttachment,
         'attachDocument':attachDocument,
         'removeAttachment':removeAttachment,
         'importDocument':importDocument,
         'insertListItem':insertListItem,
         'insertCard':insertCard,
         'recap':getRiepilogo,

         #search Cards
         'searchCards':getSearchCards,
         'searchCardsResult':getSearchCardsResult,
         'sendCard':sendCard,
         'attachDocumentjson':attachDocumentjson,

         #detail Cards
         'getIndexesDetail':getIndexesDetail,
         'saveIndexesData':saveIndexesData,
         'modifyIndexes':modifyIndexes,
         'getAdditivesDetail':getAdditivesDetail,
         'modifyAdditives':modifyAdditives,
         'saveAdditivesData':saveAdditivesData,
         'cardMenu':cardMenu,
         'signAdditive':signAdditive,
         
         #workflow
         'getActivitiesToDo':getActivitiesToDo,
         'getActivitiesInCharge':getActivitiesInCharge,
         'takeInCharge':takeInCharge,
         'forward':forward,
         'refuse':refuse,
         'getActivity':getActivity,
         'activityToDo':activityToDo,
         'activityInCharge':activityInCharge,
         
         #MFP interface
         'acquireMasterDoc':acquireMasterDoc,
         'acquireAttachment':acquireAttachment,
         'showAllCardFiles':showAllCardFiles,
         'getScan':getScan,
         'getPrint':getPrint,
         'getScanAllegati':getScanAttachments,
         'getScanAllegatiSearch':getScanAttachmentsSearch,
         'showAllCardFiles':showAllCardFiles,
         'deleteFile':deleteFile,
         'saveFile':saveFile,
         'checkStatus':checkStatus,
         'checkFile':checkFile,
         #old views
         'acquire':acquire,
         'print':printDocument,
         'saveDocument':saveDocument,
         'scan':scanDocument,
         
         #page not found
         '404' : get404
        }
#pass urls to dispatcher
urls.setUrls(newUrls)
#print("Content-Type: text/html;charset=UTF-8")
#print('\n')
#print('hello')
