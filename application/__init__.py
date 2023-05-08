import os

from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static", static_folder="static")

import pandas as pd

workbook_accounts = pd.read_csv('Accounts.csv', encoding='utf-8')
workbook_sources = pd.read_csv('Sources.csv', encoding='utf-8')
workbook_objects = pd.read_csv('GeneralObjects.csv', encoding='utf-8')
workbook_information_objects = pd.read_csv('InformationObjects.csv', encoding='utf-8')
workbook_terms = pd.read_csv('Ontology.csv', encoding='utf-8')
workbook_records = pd.read_csv('Records.csv', encoding='utf-8')
workbook_art_object_roles = pd.read_csv('ArtObjectRoles.csv', encoding='utf-8')
workbook_object_roles = pd.read_csv('ObjectRoles.csv', encoding='utf-8')
workbook_event_roles = pd.read_csv('EventRoles.csv', encoding='utf-8')
workbook_art_objects = pd.read_csv('ArtObjects.csv', encoding='utf-8')
workbook_events = pd.read_csv('Events.csv', encoding='utf-8')

workbook_accounts = workbook_accounts.to_records()
workbook_sources = workbook_sources.to_records()
workbook_objects = workbook_objects.to_records()
workbook_information_objects = workbook_information_objects.to_records()
workbook_terms = workbook_terms.to_records()
workbook_records = workbook_records.to_records()
workbook_object_roles = workbook_object_roles.to_records()
workbook_art_object_roles = workbook_art_object_roles.to_records()
workbook_event_roles = workbook_event_roles.to_records()
workbook_art_objects = workbook_art_objects.to_records()
workbook_events = workbook_events.to_records()

account_data = {}
for account in workbook_accounts:
    account_data[account[1]] = account  

source_data = {}
for source in workbook_sources:
    source_data[source[1]] = source 

general_object_data = {}   
for general_object in workbook_objects:
    general_object_data[general_object[1]] = general_object  

information_object_data = {}
for information_object in workbook_information_objects:
    information_object_data[information_object[1]] = information_object      

term_data = {}
for term in workbook_terms:
    term_data[term[1]] = term   

record_data = {}  
for record in workbook_records:
    record_data[record[1]] = record   

object_role_data = {}
for object_role in workbook_object_roles:
    object_role_data[object_role[1]] = object_role 

art_object_role_data = {}
for art_object_role in workbook_art_object_roles:
    art_object_role_data[art_object_role[1]] = art_object_role      

event_role_data = {}
for event_role in workbook_event_roles:
    event_role_data[event_role[1]] = event_role  

art_object_data = {}
for art_object in workbook_art_objects:
    art_object_data[art_object[1]] = art_object   

event_data = {}    
for event in workbook_events:
    event_data[event[1]] = event
 
@app.route("/test.html")
def test():
    return render_template("test.html",
    term_data=term_data,
    account_data = account_data,
    source_data = source_data,
    general_object_data = general_object_data,    
    information_object_data = information_object_data,
    record_data = record_data,
    object_role_data = object_role_data,
    art_object_role_data = art_object_role_data,
    event_role_data = event_role_data,
    art_object_data = art_object_data,
    event_data = event_data
    )

@app.route("/informationobject/<IRI>.html")  
def informationobject(IRI):
   information_object = information_object_data[IRI]
   type1=term_data[information_object[3]]
   type2=term_data[information_object[4]]
   type3=term_data[information_object[5]]
   type4=term_data[information_object[6]]
   if information_object[7]==information_object[7]:
    type5=term_data[information_object[7]]
   else:
    type5=term_data['FAILSAFE']
   return render_template("informationobject.html",
   label=information_object[2],
#The suffix 'L' denotes 'label'   
   type1L=type1[2],
   type2L=type2[2],
   type3L=type3[2],
   type4L=type4[2],
   type5L=type5[2],
   comment=information_object[8],
   
   type1_link='/term/'+type1[1]+'.html',
   type2_link='/term/'+type2[1]+'.html',
   type3_link='/term/'+type3[1]+'.html',
   type4_link='/term/'+type4[1]+'.html',
   type5_link='/term/'+type5[1]+'.html',
   )

@app.route("/account/<IRI>.html")   
def account(IRI):
   account = account_data[IRI]
   type1=term_data[account[3]]
   type2=term_data[account[4]]
   type3=term_data[account[5]]
   degreeOfRemove=information_object_data[account[6]]
   portraitProduction=event_data[account[7]]
   record=record_data[account[8]]
   source=source_data[account[9]]
   return render_template("account.html",
   label=account[2],
   type1L=type1[2],
   type2L=type2[2],
   type3L=type3[2],
   degreeOfRemoveL=degreeOfRemove[2],
   portraitProductionL=portraitProduction[2],
   recordL=record[2],
   sourceL=source[2],
   startPage=account[10],
   endPage=account[11],
   text=account[12],
   
   type1_link='/term/'+type1[1]+'.html',
   type2_link='/term/'+type2[1]+'.html',
   type3_link='/term/'+type3[1]+'.html',
   degreeOfRemove_link='/informationobject/'+degreeOfRemove[1]+'.html',
   portraitProduction_link='/event/'+portraitProduction[1]+'.html',
   record_link='/record/'+record[1]+'.html',
   source_link='/source/'+source[1]+'.html',
   )

@app.route("/artobject/<IRI>.html")  
def artobject(IRI):
   art_object = art_object_data[IRI]
   type1=term_data[art_object[3]]
   type2=term_data[art_object[4]]
   type3=term_data[art_object[5]]
   type4=term_data[art_object[6]]
   if art_object[7]==art_object[7]:
    type5=term_data[art_object[7]]
   else:
    type5=term_data['FAILSAFE']
   if art_object[8]==art_object[8]:
    type6=term_data[art_object[8]]
   else:
    type6=term_data['FAILSAFE']
   if art_object[9]==art_object[9]:
    type7=term_data[art_object[9]]
   else:
    type7=term_data['FAILSAFE']
   if art_object[10]==art_object[10]:
    medium=information_object_data[art_object[10]]
   else:
    medium=information_object_data['FAILSAFE']
   if art_object[15]==art_object[15]:
    collection=general_object_data[art_object[15]]
   else:
    collection=general_object_data['FAILSAFE']
   if art_object[16]==art_object[16]:
    formatFigure=information_object_data[art_object[16]]
   else:
    formatFigure=information_object_data['FAILSAFE']
   if art_object[17]==art_object[17]:
    colourPalette=information_object_data[art_object[17]]
   else:
    colourPalette=information_object_data['FAILSAFE']
   if art_object[18]==art_object[18]:
    markMakingStyle=information_object_data[art_object[18]]
   else:
    markMakingStyle=information_object_data['FAILSAFE']
   if art_object[19]==art_object[19]:
    finishedState=information_object_data[art_object[19]]
   else:
    finishedState=information_object_data['FAILSAFE']
   if art_object[20]==art_object[20]:
    conditionState=information_object_data[art_object[20]]
   else:
    conditionState=information_object_data['FAILSAFE']
   if art_object[21]==art_object[21]:
    record=record_data[art_object[21]]
   else:
    record=record_data['FAILSAFE']
   if art_object[22]==art_object[22]:
    relatedRecord=record_data[art_object[22]]
   else:
    relatedRecord=record_data['FAILSAFE']
   if art_object[23]==art_object[23]:
    artObjectRole=art_object_role_data[art_object[23]]
   else:
    artObjectRole=art_object_role_data['FAILSAFE']
   if art_object[24]==art_object[24]:
    artObjectRole1=art_object_role_data[art_object[24]]
   else:
    artObjectRole1=art_object_role_data['FAILSAFE']
   if art_object[25]==art_object[25]:
    artObjectRole2=art_object_role_data[art_object[25]]
   else:
    artObjectRole2=art_object_role_data['FAILSAFE']
   if art_object[26]==art_object[26]:
    artObjectRole3=art_object_role_data[art_object[26]]
   else:
    artObjectRole3=art_object_role_data['FAILSAFE']
   if art_object[27]==art_object[27]:
    artObjectRole4=art_object_role_data[art_object[27]]
   else:
    artObjectRole4=art_object_role_data['FAILSAFE']
   if art_object[29]==art_object[29]:
    relatedArtObject=art_object_data[art_object[29]]
   else:
    relatedArtObject=art_object_role_data['FAILSAFE']
   if art_object[30]==art_object[30]:
    relatedArtObject1=art_object_data[art_object[30]]
   else:
    relatedArtObject1=art_object_role_data['FAILSAFE']
   if art_object[31]==art_object[31]:
    relatedArtObject2=art_object_data[art_object[31]]
   else:
    relatedArtObject2=art_object_role_data['FAILSAFE']
   if art_object[32]==art_object[32]:
    relatedArtObject3=art_object_data[art_object[32]]
   else:
    relatedArtObject3=art_object_role_data['FAILSAFE']
   if art_object[33]==art_object[33]:
    relatedArtObject4=art_object_data[art_object[33]]
   else:
    relatedArtObject4=art_object_role_data['FAILSAFE']
   if art_object[34]==art_object[34]:
    relatedArtObject5=art_object_data[art_object[34]]
   else:
    relatedArtObject5=art_object_role_data['FAILSAFE']
   if art_object[35]==art_object[35]:
    relatedArtObject6=art_object_data[art_object[35]]
   else:
    relatedArtObject6=art_object_role_data['FAILSAFE']
   if art_object[36]==art_object[36]:
    relatedArtObject7=art_object_data[art_object[36]]
   else:
    relatedArtObject7=art_object_role_data['FAILSAFE']
   if art_object[37]==art_object[37]:
    relatedArtObject8=art_object_data[art_object[37]]
   else:
    relatedArtObject8=art_object_role_data['FAILSAFE']
   if art_object[38]==art_object[38]:
    relatedArtObject9=art_object_data[art_object[38]]
   else:
    relatedArtObject9=art_object_role_data['FAILSAFE']
   if art_object[39]==art_object[39]:
    relatedArtObject10=art_object_data[art_object[39]]
   else:
    relatedArtObject10=art_object_role_data['FAILSAFE']
   if art_object[40]==art_object[40]:
    relatedArtObject11=art_object_data[art_object[40]]
   else:
    relatedArtObject11=art_object_role_data['FAILSAFE']
   if art_object[41]==art_object[41]:
    relatedArtObject12=art_object_data[art_object[41]]
   else:
    relatedArtObject12=art_object_role_data['FAILSAFE']
   if art_object[42]==art_object[42]:
    relatedArtObject13=art_object_data[art_object[42]]
   else:
    relatedArtObject13=art_object_role_data['FAILSAFE']
   if art_object[43]==art_object[43]:
    relatedArtObject14=art_object_data[art_object[43]]
   else:
    relatedArtObject14=art_object_role_data['FAILSAFE']
   if art_object[44]==art_object[44]:
    relatedArtObject15=art_object_data[art_object[44]]
   else:
    relatedArtObject15=art_object_role_data['FAILSAFE']
   if art_object[45]==art_object[45]:
    relatedArtObject16=art_object_data[art_object[45]]
   else:
    relatedArtObject16=art_object_role_data['FAILSAFE']
   if art_object[46]==art_object[46]:
    relatedArtObject17=art_object_data[art_object[46]]
   else:
    relatedArtObject17=art_object_role_data['FAILSAFE']
   if art_object[47]==art_object[47]:
    relatedArtObject18=art_object_data[art_object[47]]
   else:
    relatedArtObject18=art_object_role_data['FAILSAFE']
   if art_object[48]==art_object[48]:
    relatedArtObject19=art_object_data[art_object[48]]
   else:
    relatedArtObject19=art_object_role_data['FAILSAFE']
   if art_object[55]==art_object[55]:
    sameEntity=art_object_data[art_object[55]]
   else:
    sameEntity=art_object_role_data['FAILSAFE']
   return render_template("artobject.html",
   label=art_object[2],
   image='/static/img/'+IRI+'.jpg',
   
   type1L=type1[2],
   type2L=type2[2],
   type3L=type3[2],
   type4L=type4[2],
   type5L=type5[2],
   type6L=type6[2],
   type7L=type7[2],
   HeightInMm=art_object[11],
   WidthInMm=art_object[12],
   DepthInMm=art_object[13],
   DiameterInMm=art_object[14],
   mediumL=medium[2],
   collectionL=collection[2],
   formatFigureL=formatFigure[2],
   colourPaletteL=colourPalette[2],
   markMakingStyleL=markMakingStyle[2],
   finishedStateL=finishedState[2],
   conditionStateL=conditionState[2],
   recordL=record[2],
   relatedRecordL=relatedRecord[2],
   artObjectRoleL=artObjectRole[2],
   artObjectRole1L=artObjectRole1[2],
   artObjectRole2L=artObjectRole2[2],
   artObjectRole3L=artObjectRole3[2],
   artObjectRole4L=artObjectRole4[2],
   ImageCreditLine=art_object[28],
   relatedArtObjectL=relatedArtObject[2],
   relatedArtObject1L=relatedArtObject1[2],
   relatedArtObject2L=relatedArtObject2[2],
   relatedArtObject3L=relatedArtObject3[2],
   relatedArtObject4L=relatedArtObject4[2],
   relatedArtObject5L=relatedArtObject5[2],
   relatedArtObject6L=relatedArtObject6[2],
   relatedArtObject7L=relatedArtObject7[2],
   relatedArtObject8L=relatedArtObject8[2],
   relatedArtObject9L=relatedArtObject9[2],
   relatedArtObject10L=relatedArtObject10[2],
   relatedArtObject11L=relatedArtObject11[2],
   relatedArtObject12L=relatedArtObject12[2],
   relatedArtObject13L=relatedArtObject13[2],
   relatedArtObject14L=relatedArtObject14[2],
   relatedArtObject15L=relatedArtObject15[2],
   relatedArtObject16L=relatedArtObject16[2],
   relatedArtObject17L=relatedArtObject17[2],
   relatedArtObject18L=relatedArtObject18[2],
   relatedArtObject19L=relatedArtObject19[2],
   link=art_object[53],
   link1=art_object[54],
   sameEntityL=sameEntity[2],

   type1_link='/term/'+type1[1]+'.html',
   type2_link='/term/'+type2[1]+'.html',
   type3_link='/term/'+type3[1]+'.html',
   type4_link='/term/'+type4[1]+'.html',
   type5_link='/term/'+type5[1]+'.html',
   type6_link='/term/'+type6[1]+'.html',
   type7_link='/term/'+type7[1]+'.html',
   medium_link='/informationobject/'+medium[1]+'.html',
   collection_link='/object/'+collection[1]+'.html',
   formatFigure_link='/informationobject/'+formatFigure[1]+'.html',
   colourPalette_link='/informationobject/'+colourPalette[1]+'.html',
   markMakingStyle_link='/informationobject/'+markMakingStyle[1]+'.html',
   finishedState_link='/informationobject/'+finishedState[1]+'.html',
   conditionState_link='/informationobject/'+conditionState[1]+'.html',
   record_link='/record/'+record[1]+'.html',
   relatedRecord_link='/record/'+relatedRecord[1]+'.html',
   artObjectRole_link='/artobjectrole/'+artObjectRole[1]+'.html',
   artObjectRole1_link='/artobjectrole/'+artObjectRole1[1]+'.html',
   artObjectRole2_link='/artobjectrole/'+artObjectRole2[1]+'.html',
   artObjectRole3_link='/artobjectrole/'+artObjectRole3[1]+'.html',
   artObjectRole4_link='/artobjectrole/'+artObjectRole4[1]+'.html',
   relatedArtObject_link='/artobject/'+relatedArtObject[1]+'.html',
   relatedArtObject1_link='/artobject/'+relatedArtObject1[1]+'.html',
   relatedArtObject2_link='/artobject/'+relatedArtObject2[1]+'.html',
   relatedArtObject3_link='/artobject/'+relatedArtObject3[1]+'.html',
   relatedArtObject4_link='/artobject/'+relatedArtObject4[1]+'.html',
   relatedArtObject5_link='/artobject/'+relatedArtObject5[1]+'.html',
   relatedArtObject6_link='/artobject/'+relatedArtObject6[1]+'.html',
   relatedArtObject7_link='/artobject/'+relatedArtObject7[1]+'.html',
   relatedArtObject8_link='/artobject/'+relatedArtObject8[1]+'.html',
   relatedArtObject9_link='/artobject/'+relatedArtObject9[1]+'.html',
   relatedArtObject10_link='/artobject/'+relatedArtObject10[1]+'.html',
   relatedArtObject11_link='/artobject/'+relatedArtObject11[1]+'.html',
   relatedArtObject12_link='/artobject/'+relatedArtObject12[1]+'.html',
   relatedArtObject13_link='/artobject/'+relatedArtObject13[1]+'.html',
   relatedArtObject14_link='/artobject/'+relatedArtObject14[1]+'.html',
   relatedArtObject15_link='/artobject/'+relatedArtObject15[1]+'.html',
   relatedArtObject16_link='/artobject/'+relatedArtObject16[1]+'.html',
   relatedArtObject17_link='/artobject/'+relatedArtObject17[1]+'.html',
   relatedArtObject18_link='/artobject/'+relatedArtObject18[1]+'.html',
   relatedArtObject19_link='/artobject/'+relatedArtObject19[1]+'.html',
   sameEntity_link='/artobject/'+sameEntity[1]+'.html',
  )
    
@app.route("/source/<IRI>.html")    
def source(IRI):
    source=source_data[IRI]
    type1=term_data[source[3]]
    type2=term_data[source[4]]
    type3=term_data[source[5]]
    if source[6]==source[6]:
     type4=term_data[source[6]]
    else:
     type4=term_data['FAILSAFE']
    if source[8]==source[8]:
     protagonist=general_object_data[source[8]]
    else:
     protagonist=general_object_data['FAILSAFE']
    if source[9]==source[9]:
     protagonist1=general_object_data[source[9]]
    else:
     protagonist1=general_object_data['FAILSAFE']
    if source[10]==source[10]:
     authorOrSpeaker=general_object_data[source[10]]
    else:
     authorOrSpeaker=general_object_data['FAILSAFE']
    if source[11]==source[11]:
     authorOrSpeaker1=general_object_data[source[11]]
    else:
     authorOrSpeaker1=general_object_data['FAILSAFE']
    if source[12]==source[12]:
     interviewerOrRecipient=general_object_data[source[12]]
    else:
     interviewerOrRecipient=general_object_data['FAILSAFE']
    if source[13]==source[13]:
     editor=general_object_data[source[13]]
    else:
     editor=general_object_data['FAILSAFE']
    if source[14]==source[14]:
     editor1=general_object_data[source[14]]
    else:
     editor1=general_object_data['FAILSAFE']
    if source[15]==source[15]:
     editor2=general_object_data[source[15]]
    else:
     editor2=general_object_data['FAILSAFE']
    if source[16]==source[16]:
     publisher=general_object_data[source[16]]
    else:
     publisher=general_object_data['FAILSAFE']
    if source[17]==source[17]:
     publicationStatus=information_object_data[source[17]]
    else:
     publicationStatus=information_object_data['FAILSAFE']
    if source[20]==source[20]:
     sourceFormat=information_object_data[source[20]]
    else:
     sourceFormat=information_object_data['FAILSAFE']
    if source[21]==source[21]:
     accessChannel=information_object_data[source[21]]
    else:
     accessChannel=information_object_data['FAILSAFE']
    if source[27]==source[27]:
     account=account_data[source[27]]
    else:
     source=information_object_data['FAILSAFE']
    if source[28]==source[28]:
     account1=account_data[source[28]]
    else:
     account1=account_data['FAILSAFE']
    if source[29]==source[29]:
     account2=account_data[source[29]]
    else:
     account2=account_data['FAILSAFE']
    if source[30]==source[30]:
     account3=account_data[source[30]]
    else:
     account3=account_data['FAILSAFE']
    if source[31]==source[31]:
     account4=account_data[source[31]]
    else:
     account4=account_data['FAILSAFE']
    if source[32]==source[32]:
     account5=account_data[source[32]]
    else:
     account5=account_data['FAILSAFE']
    if source[33]==source[33]:
     account6=account_data[source[33]]
    else:
     account6=account_data['FAILSAFE']
    if source[34]==source[34]:
     account7=account_data[source[34]]
    else:
     account7=account_data['FAILSAFE']
    if source[35]==source[35]:
     account8=account_data[source[35]]
    else:
     account8=account_data['FAILSAFE']
    if source[36]==source[36]:
     account9=account_data[source[36]]
    else:
     account9=account_data['FAILSAFE']
    if source[37]==source[37]:
     account10=account_data[source[37]]
    else:
     account10=account_data['FAILSAFE']
    if source[38]==source[38]:
     account11=account_data[source[38]]
    else:
     account11=account_data['FAILSAFE']
    if source[39]==source[39]:
     account12=account_data[source[39]]
    else:
     account12=account_data['FAILSAFE']
    if source[40]==source[40]:
     account13=account_data[source[40]]
    else:
     account13=account_data['FAILSAFE']
    if source[41]==source[41]:
     account14=account_data[source[41]]
    else:
     account14=account_data['FAILSAFE']
    return render_template("source.html",
    label=source[2],
    
    type1L= type1[2],
    type2L=type2[2],
    type3L=type3[2],
    type4L=type4[2],
    title=source[7],
    protagonistL=protagonist[2],
    protagonist1L=protagonist1[2],
    authorOrSpeakerL=authorOrSpeaker[2],
    authorOrSpeaker1L=authorOrSpeaker1[2],
    interviewerOrRecipientL=interviewerOrRecipient[2],
    editorL=editor[2],
    editor1L=editor1[2],
    editor2L=editor2[2],
    publisherL=publisher[2],
    publicationStatusL=publicationStatus[2],
    PublishedDate=source[18],
    FirstPublishedDate=source[19],
    sourceFormatL=sourceFormat[2],
    accessChannelL=accessChannel[2],
    URL=source[22],
    dateURLAccessed=source[23],
    archiveName=source[24],
    archiveReference=source[25],
    comment=source[26],
    accountL=account[2],
    account1L=account1[2],
    account2L=account2[2],
    account3L=account3[2],
    account4L=account4[2],
    account5L=account5[2],
    account6L=account6[2],
    account7L=account7[2],
    account8L=account8[2],
    account9L=account9[2],
    account10L=account10[2],
    account11L=account11[2],
    account12L=account12[2],
    account13L=account13[2],
    account14L=account14[2],
    
    type1_link='/term/'+type1[1]+'.html',
    type2_link='/term/'+type2[1]+'.html',
    type3_link='/term/'+type3[1]+'.html',
    type4_link='/term/'+type4[1]+'.html',
    protagonist_link='/object/'+protagonist[1]+'.html',
    protagonist1_link='/object/'+protagonist1[1]+'.html',
    authorOrSpeaker_link='/object/'+authorOrSpeaker[1]+'.html',
    authorOrSpeaker1_link='/object/'+authorOrSpeaker1[1]+'.html',
    interviewerOrRecipient_link='/object/'+interviewerOrRecipient[1]+'.html',
    editor_link='/object/'+editor[1]+'.html',
    editor1_link='/object/'+editor1[1]+'.html',
    editor2_link='/object/'+editor2[1]+'.html',
    publisher_link='/object/'+publisher[1]+'.html',
    publicationStatus_link='/informationobject/'+publicationStatus[1]+'.html',
    sourceFormat_link='/informationobject/'+sourceFormat[1]+'.html',
    accessChannel_link='/informationobject/'+accessChannel[1]+'.html',
    account_link='/account/'+account[1]+'.html',
    account1_link='/account/'+account1[1]+'.html',
    account2_link='/account/'+account2[1]+'.html',
    account3_link='/account/'+account3[1]+'.html',
    account4_link='/account/'+account4[1]+'.html',
    account5_link='/account/'+account5[1]+'.html',
    account6_link='/account/'+account6[1]+'.html',
    account7_link='/account/'+account7[1]+'.html',
    account8_link='/account/'+account8[1]+'.html',
    account9_link='/account/'+account9[1]+'.html',
    account10_link='/account/'+account10[1]+'.html',
    account11_link='/account/'+account11[1]+'.html',
    account12_link='/account/'+account12[1]+'.html',
    account13_link='/account/'+account13[1]+'.html',
    account14_link='/account/'+account14[1]+'.html',
   )

@app.route("/artobjectrole/<IRI>.html")   
def artobjectrole(IRI):
    art_object_role = art_object_role_data[IRI]
    type1=term_data[art_object_role[3]]
    type2=term_data[art_object_role[4]]
    type3=term_data[art_object_role[5]]
    type4=term_data[art_object_role[6]]
    if art_object_role[7]==art_object_role[7]:
      type5=term_data[art_object_role[7]]
    else:
     type5=term_data['FAILSAFE']
    if art_object_role[8]==art_object_role[8]:
      type6=term_data[art_object_role[8]]
    else:
     type6=term_data['FAILSAFE']
    if art_object_role[9]==art_object_role[9]:
      type7=term_data[art_object_role[9]]
    else:
     type7=term_data['FAILSAFE']
    if art_object_role[10]==art_object_role[10]:
      type8=term_data[art_object_role[10]]
    else:
     type8=term_data['FAILSAFE']
    event=event_data[art_object_role[11]]
    if art_object_role[12]==art_object_role[12]:
      event1=event_data[art_object_role[12]]
    else:
     event1=event_data['FAILSAFE']
    if art_object_role[13]==art_object_role[13]:
      event2=event_data[art_object_role[13]]
    else:
     event2=event_data['FAILSAFE']
    artObject=art_object_data[art_object_role[14]]
    if art_object_role[15]==art_object_role[15]:
      decisionMaker=object_role_data[art_object_role[15]]
    else:
     decisionMaker=object_role_data['FAILSAFE']
    if art_object_role[16]==art_object_role[16]:
      decisionMaker1=object_role_data[art_object_role[16]]
    else:
     decisionMaker1=object_role_data['FAILSAFE']
    if art_object_role[17]==art_object_role[17]:
      decisionMaker2=object_role_data[art_object_role[17]]
    else:
     decisionMaker2=object_role_data['FAILSAFE']
    if art_object_role[18]==art_object_role[18]:
      decisionMaker3=object_role_data[art_object_role[18]]
    else:
     decisionMaker3=object_role_data['FAILSAFE']
    if art_object_role[19]==art_object_role[19]:
      decisionMaker4=object_role_data[art_object_role[19]]
    else:
     decisionMaker4=object_role_data['FAILSAFE']
    if art_object_role[20]==art_object_role[20]:
      sameEntity=art_object_role_data[art_object_role[20]]
    else:
     sameEntity=art_object_role_data['FAILSAFE']
    return render_template("artobjectrole.html",
    label=art_object_role[2],
    
    type1L=type1[2],
    type2L=type2[2],
    type3L=type3[2],
    type4L=type4[2],
    type5L=type5[2],
    type6L=type6[2],
    type7L=type7[2],
    type8L=type8[2],
    eventL=event[2],
    event1L=event1[2],
    event2L=event2[2],
    artObjectL=artObject[2],
    decisionMakerL=decisionMaker[2],
    decisionMaker1L=decisionMaker1[2],
    decisionMaker2L=decisionMaker2[2],
    decisionMaker3L=decisionMaker3[2],
    decisionMaker4L=decisionMaker4[2],
    sameEntityL=sameEntity[2],
    
    type1_link='/term/'+type1[1]+'.html',
    type2_link='/term/'+type2[1]+'.html',
    type3_link='/term/'+type3[1]+'.html',
    type4_link='/term/'+type4[1]+'.html',
    type5_link='/term/'+type5[1]+'.html',
    type6_link='/term/'+type6[1]+'.html',
    type7_link='/term/'+type7[1]+'.html',
    type8_link='/term/'+type8[1]+'.html',
    event_link='/event/'+event[1]+'.html',
    event1_link='/event/'+event1[1]+'.html',
    event2_link='/event/'+event2[1]+'.html',
    artObject_link='/artobject/'+artObject[1]+'.html',
    decisionMaker_link='/objectrole/'+decisionMaker[1]+'.html',
    decisionMaker1_link='/objectrole/'+decisionMaker1[1]+'.html',
    decisionMaker2_link='/objectrole/'+decisionMaker2[1]+'.html',
    decisionMaker3_link='/objectrole/'+decisionMaker3[1]+'.html',
    decisionMaker4_link='/objectrole/'+decisionMaker4[1]+'.html',
    sameEntity_link='/artobjectrole/'+sameEntity[1]+'.html',
   )
   
@app.route("/record/<IRI>.html")    
def record(IRI):
    record = record_data[IRI]
    type1=term_data[record[3]]
    type2=term_data[record[4]]
    type3=term_data[record[5]]
    portraitProduction=event_data[record[6]]
    portraitSittingAccount=account_data[record[7]]
    if record[8]==record[8]:
     portraitSittingAccount1=account_data[record[8]]
    else:
     portraitSittingAccount1=account_data['FAILSAFE']
    if record[9]==record[9]:
     portraitSittingAccount2=account_data[record[9]]
    else:
     portraitSittingAccount2=account_data['FAILSAFE']
    if record[10]==record[10]:
     portraitSittingAccount3=account_data[record[10]]
    else:
     portraitSittingAccount3=account_data['FAILSAFE']
    if record[11]==record[11]:
     portraitSittingAccount4=account_data[record[11]]
    else:
     portraitSittingAccount4=account_data['FAILSAFE']
    if record[12]==record[12]:
     portraitSittingAccount5=account_data[record[12]]
    else:
     portraitSittingAccount5=account_data['FAILSAFE']
    if record[13]==record[13]:
     portraitSittingAccount6=account_data[record[13]]
    else:
     portraitSittingAccount6=account_data['FAILSAFE']
    if record[14]==record[14]:
     portraitSittingAccount7=account_data[record[14]]
    else:
     portraitSittingAccount7=account_data['FAILSAFE']
    if record[15]==record[15]:
     portraitSittingAccount8=account_data[record[15]]
    else:
     portraitSittingAccount8=account_data['FAILSAFE']
    if record[16]==record[16]:
     portraitSittingAccount9=account_data[record[16]]
    else:
     portraitSittingAccount9=account_data['FAILSAFE']
    if record[17]==record[17]:
     portraitSittingAccount10=account_data[record[17]]
    else:
     portraitSittingAccount10=account_data['FAILSAFE']
    if record[18]==record[18]:
     portraitSittingAccount11=account_data[record[18]]
    else:
     portraitSittingAccount11=account_data['FAILSAFE']
    if record[19]==record[19]:
     portraitSittingAccount12=account_data[record[19]]
    else:
     portraitSittingAccount12=account_data['FAILSAFE']
    if record[20]==record[20]:
     portraitSittingAccount13=account_data[record[20]]
    else:
     portraitSittingAccount13=account_data['FAILSAFE']
    if record[21]==record[21]:
     portraitSittingAccount14=account_data[record[21]]
    else:
     portraitSittingAccount14=account_data['FAILSAFE']
    if record[22]==record[22]:
     portraitSittingAccount15=account_data[record[22]]
    else:
     portraitSittingAccount15=account_data['FAILSAFE']
    portraitObject=art_object_data[record[23]]
    if record[24]==record[24]:
     relatedObject=art_object_data[record[24]]
    else:
     relatedObject=art_object_data['FAILSAFE']
    if record[25]==record[25]:
     relatedObject1=art_object_data[record[25]]
    else:
     relatedObject1=art_object_data['FAILSAFE']
    if record[26]==record[26]:
     relatedObject2=art_object_data[record[26]]
    else:
     relatedObject2=art_object_data['FAILSAFE']
    if record[27]==record[27]:
     relatedObject3=art_object_data[record[27]]
    else:
     relatedObject3=art_object_data['FAILSAFE']
    if record[28]==record[28]:
     relatedObject4=art_object_data[record[28]]
    else:
     relatedObject4=art_object_data['FAILSAFE']
    if record[29]==record[29]:
     relatedObject5=art_object_data[record[29]]
    else:
     relatedObject5=art_object_data['FAILSAFE']
    if record[30]==record[30]:
     relatedObject6=art_object_data[record[30]]
    else:
     relatedObject6=art_object_data['FAILSAFE']
    if record[31]==record[31]:
     relatedObject7=art_object_data[record[31]]
    else:
     relatedObject7=art_object_data['FAILSAFE']
    if record[32]==record[32]:
     relatedObject8=art_object_data[record[32]]
    else:
     relatedObject8=art_object_data['FAILSAFE']
    if record[33]==record[33]:
     relatedObject9=art_object_data[record[33]]
    else:
     relatedObject9=art_object_data['FAILSAFE']
    if record[34]==record[34]:
     relatedObject10=art_object_data[record[34]]
    else:
     relatedObject10=art_object_data['FAILSAFE']
    if record[35]==record[35]:
     relatedObject11=art_object_data[record[35]]
    else:
     relatedObject11=art_object_data['FAILSAFE']
    if record[36]==record[36]:
     relatedObject12=art_object_data[record[36]]
    else:
     relatedObject12=art_object_data['FAILSAFE']
    return render_template("record.html",
    label=record[2],
    
    type1L=type1[2],
    type2L=type2[2],
    type3L=type3[2],
    portraitProductionL=portraitProduction[2],
    portraitSittingAccountL=portraitSittingAccount[2],
    portraitSittingAccount1L=portraitSittingAccount1[2],
    portraitSittingAccount2L=portraitSittingAccount2[2],
    portraitSittingAccount3L=portraitSittingAccount3[2],
    portraitSittingAccount4L=portraitSittingAccount4[2],
    portraitSittingAccount5L=portraitSittingAccount5[2],
    portraitSittingAccount6L=portraitSittingAccount6[2],
    portraitSittingAccount7L=portraitSittingAccount7[2],
    portraitSittingAccount8L=portraitSittingAccount8[2],
    portraitSittingAccount9L=portraitSittingAccount9[2],
    portraitSittingAccount10L=portraitSittingAccount10[2],
    portraitSittingAccount11L=portraitSittingAccount11[2],
    portraitSittingAccount12L=portraitSittingAccount12[2],
    portraitSittingAccount13L=portraitSittingAccount13[2],
    portraitSittingAccount14L=portraitSittingAccount14[2],
    portraitSittingAccount15L=portraitSittingAccount15[2],
    portraitObjectL=portraitObject[2],
    relatedObjectL=relatedObject[2],
    relatedObject1L=relatedObject1[2],
    relatedObject2L=relatedObject2[2],
    relatedObject3L=relatedObject3[2],
    relatedObject4L=relatedObject4[2],
    relatedObject5L=relatedObject5[2],
    relatedObject6L=relatedObject6[2],
    relatedObject7L=relatedObject7[2],
    relatedObject8L=relatedObject8[2],
    relatedObject9L=relatedObject9[2],
    relatedObject10L=relatedObject10[2],
    relatedObject11L=relatedObject11[2],
    relatedObject12L=relatedObject12[2],
    
    type1_link='/term/'+type1[1]+'.html',
    type2_link='/term/'+type2[1]+'.html',
    type3_link='/term/'+type3[1]+'.html',
    portraitProduction_link='/event/'+portraitProduction[1]+'.html',
    portraitSittingAccount_link='/account/'+portraitSittingAccount[1]+'.html',
    portraitSittingAccount1_link='/account/'+portraitSittingAccount1[1]+'.html',
    portraitSittingAccount2_link='/account/'+portraitSittingAccount2[1]+'.html',
    portraitSittingAccount3_link='/account/'+portraitSittingAccount3[1]+'.html',
    portraitSittingAccount4_link='/account/'+portraitSittingAccount4[1]+'.html',
    portraitSittingAccount5_link='/account/'+portraitSittingAccount5[1]+'.html',
    portraitSittingAccount6_link='/account/'+portraitSittingAccount6[1]+'.html',
    portraitSittingAccount7_link='/account/'+portraitSittingAccount7[1]+'.html',
    portraitSittingAccount8_link='/account/'+portraitSittingAccount8[1]+'.html',
    portraitSittingAccount9_link='/account/'+portraitSittingAccount9[1]+'.html',
    portraitSittingAccount10_link='/account/'+portraitSittingAccount10[1]+'.html',
    portraitSittingAccount11_link='/account/'+portraitSittingAccount11[1]+'.html',
    portraitSittingAccount12_link='/account/'+portraitSittingAccount12[1]+'.html',
    portraitSittingAccount13_link='/account/'+portraitSittingAccount13[1]+'.html',
    portraitSittingAccount14_link='/account/'+portraitSittingAccount14[1]+'.html',
    portraitSittingAccount15_link='/account/'+portraitSittingAccount15[1]+'.html',
    portraitObject_link='/artobject/'+portraitObject[1]+'.html',
    relatedObject_link='/artobject/'+relatedObject[1]+'.html',
    relatedObject1_link='/artobject/'+relatedObject1[1]+'.html',
    relatedObject2_link='/artobject/'+relatedObject2[1]+'.html',
    relatedObject3_link='/artobject/'+relatedObject3[1]+'.html',
    relatedObject4_link='/artobject/'+relatedObject4[1]+'.html',
    relatedObject5_link='/artobject/'+relatedObject5[1]+'.html',
    relatedObject6_link='/artobject/'+relatedObject6[1]+'.html',
    relatedObject7_link='/artobject/'+relatedObject7[1]+'.html',
    relatedObject8_link='/artobject/'+relatedObject8[1]+'.html',
    relatedObject9_link='/artobject/'+relatedObject9[1]+'.html',
    relatedObject10_link='/artobject/'+relatedObject10[1]+'.html',
    relatedObject11_link='/artobject/'+relatedObject11[1]+'.html',
    relatedObject12_link='/artobject/'+relatedObject12[1]+'.html',
   )
    
@app.route("/objectrole/<IRI>.html")   
def objectrole(IRI):
    object_role = object_role_data[IRI]
    type1=term_data[object_role[3]]
    type2=term_data[object_role[4]]
    type3=term_data[object_role[5]]
    if object_role[6]==object_role[6]:
      type4=term_data[object_role[6]]
    else:
      type4=term_data['FAILSAFE']
    if object_role[7]==object_role[7]:
      type5=term_data[object_role[7]]
    else:
      type5=term_data['FAILSAFE']
    if object_role[8]==object_role[8]:
      type6=term_data[object_role[8]]
    else:
      type6=term_data['FAILSAFE']
    if object_role[9]==object_role[9]:
      type7=term_data[object_role[9]]
    else:
      type7=term_data['FAILSAFE']
    if object_role[10]==object_role[10]:
      type8=term_data[object_role[10]]
    else:
      type8=term_data['FAILSAFE']
    if object_role[11]==object_role[11]:
      type9=term_data[object_role[11]]
    else:
      type9=term_data['FAILSAFE']
    if object_role[12]==object_role[12]:
      type10=term_data[object_role[12]]
    else:
      type10=term_data['FAILSAFE']
    if object_role[13]==object_role[13]:
      type11=term_data[object_role[13]]
    else:
      type11=term_data['FAILSAFE']
    if object_role[14]==object_role[14]:
      type12=term_data[object_role[14]]
    else:
      type12=term_data['FAILSAFE']
    if object_role[15]==object_role[15]:
      type13=term_data[object_role[15]]
    else:
      type13=term_data['FAILSAFE']
    if object_role[16]==object_role[16]:
      event=event_data[object_role[16]]
    else:
      event=event_data['FAILSAFE']
    if object_role[17]==object_role[17]:
      event1=event_data[object_role[17]]
    else:
      event1=event_data['FAILSAFE']
    if object_role[18]==object_role[18]:
      event2=event_data[object_role[18]]
    else:
      event2=event_data['FAILSAFE']
    if object_role[19]==object_role[19]:
      event3=event_data[object_role[19]]
    else:
      event3=event_data['FAILSAFE']
    if object_role[20]==object_role[20]:
      event4=event_data[object_role[20]]
    else:
      event4=event_data['FAILSAFE']
    if object_role[21]==object_role[21]:
      event5=event_data[object_role[21]]
    else:
      event5=event_data['FAILSAFE']
    if object_role[22]==object_role[22]:
      event6=event_data[object_role[22]]
    else:
      event6=event_data['FAILSAFE']
    if object_role[23]==object_role[23]:
      event7=event_data[object_role[23]]
    else:
      event7=event_data['FAILSAFE']
    if object_role[24]==object_role[24]:
      event8=event_data[object_role[24]]
    else:
      event8=event_data['FAILSAFE']
    if object_role[25]==object_role[25]:
      event9=event_data[object_role[25]]
    else:
      event9=event_data['FAILSAFE']
    if object_role[26]==object_role[26]:
      event10=event_data[object_role[26]]
    else:
      event10=event_data['FAILSAFE']
    if object_role[27]==object_role[27]:
      event11=event_data[object_role[27]]
    else:
      event11=event_data['FAILSAFE']
    if object_role[28]==object_role[28]:
      event12=event_data[object_role[28]]
    else:
      event12=event_data['FAILSAFE']
    if object_role[29]==object_role[29]:
      event13=event_data[object_role[29]]
    else:
      event13=event_data['FAILSAFE']
    if object_role[30]==object_role[30]:
      event14=event_data[object_role[30]]
    else:
      event14=event_data['FAILSAFE']
    if object_role[31]==object_role[31]:
      event15=event_data[object_role[31]]
    else:
      event15=event_data['FAILSAFE']
    if object_role[32]==object_role[32]:
      event16=event_data[object_role[32]]
    else:
      event16=event_data['FAILSAFE']
    if object_role[33]==object_role[33]:
      event17=event_data[object_role[33]]
    else:
      event17=event_data['FAILSAFE']
    if object_role[34]==object_role[34]:
      event18=event_data[object_role[34]]
    else:
      event18=event_data['FAILSAFE']
    if object_role[35]==object_role[35]:
      event19=event_data[object_role[35]]
    else:
      event19=event_data['FAILSAFE']
    if object_role[45]==object_role[45]:
      object=general_object_data[object_role[45]]
    else:
      object=general_object_data['FAILSAFE']
    if object_role[46]==object_role[46]:
      object1=general_object_data[object_role[46]]
    else:
      object1=general_object_data['FAILSAFE']
    if object_role[47]==object_role[47]:
      object2=general_object_data[object_role[47]]
    else:
      object2=general_object_data['FAILSAFE']
    if object_role[48]==object_role[48]:
      object3=general_object_data[object_role[48]]
    else:
      object3=general_object_data['FAILSAFE']
    if object_role[49]==object_role[49]:
      objectRole=object_role_data[object_role[49]]
    else:
      objectRole=object_role_data['FAILSAFE']
    if object_role[50]==object_role[50]:
      objectRole1=object_role_data[object_role[50]]
    else:
      objectRole1=object_role_data['FAILSAFE']
    if object_role[51]==object_role[51]:
      objectRole2=object_role_data[object_role[51]]
    else:
      objectRole2=object_role_data['FAILSAFE']
    if object_role[52]==object_role[52]:
      objectRole3=object_role_data[object_role[52]]
    else:
      objectRole3=object_role_data['FAILSAFE']
    if object_role[53]==object_role[53]:
      objectRole4=object_role_data[object_role[53]]
    else:
      objectRole4=object_role_data['FAILSAFE']
    if object_role[54]==object_role[54]:
      objectRole5=object_role_data[object_role[54]]
    else:
      objectRole5=object_role_data['FAILSAFE']
    if object_role[55]==object_role[55]:
      objectRole6=object_role_data[object_role[55]]
    else:
      objectRole6=object_role_data['FAILSAFE']
    if object_role[56]==object_role[56]:
      objectRole7=object_role_data[object_role[56]]
    else:
      objectRole7=object_role_data['FAILSAFE']
    if object_role[57]==object_role[57]:
      objectRole8=object_role_data[object_role[57]]
    else:
      objectRole8=object_role_data['FAILSAFE']
    if object_role[58]==object_role[58]:
      objectRole9=object_role_data[object_role[58]]
    else:
      objectRole9=object_role_data['FAILSAFE']
    if object_role[59]==object_role[59]:
      objectRole10=object_role_data[object_role[59]]
    else:
      objectRole10=object_role_data['FAILSAFE']
    if object_role[60]==object_role[60]:
      objectRole11=object_role_data[object_role[60]]
    else:
      objectRole11=object_role_data['FAILSAFE']
    if object_role[61]==object_role[61]:
      objectRole12=object_role_data[object_role[61]]
    else:
      objectRole12=object_role_data['FAILSAFE']
    if object_role[62]==object_role[62]:
      objectRole13=object_role_data[object_role[62]]
    else:
      objectRole13=object_role_data['FAILSAFE']
    if object_role[63]==object_role[63]:
      objectRole14=object_role_data[object_role[63]]
    else:
      objectRole14=object_role_data['FAILSAFE']
    if object_role[64]==object_role[64]:
      objectRole15=object_role_data[object_role[64]]
    else:
      objectRole15=object_role_data['FAILSAFE']
    if object_role[65]==object_role[65]:
      objectRole16=object_role_data[object_role[65]]
    else:
      objectRole16=object_role_data['FAILSAFE']
    if object_role[66]==object_role[66]:
      objectRole17=object_role_data[object_role[66]]
    else:
      objectRole17=object_role_data['FAILSAFE']
    if object_role[67]==object_role[67]:
      objectRole18=object_role_data[object_role[67]]
    else:
      objectRole18=object_role_data['FAILSAFE']
    if object_role[68]==object_role[68]:
      objectRole19=object_role_data[object_role[68]]
    else:
      objectRole19=object_role_data['FAILSAFE']
    if object_role[79]==object_role[79]:
      relatedRole=object_role_data[object_role[79]]
    else:
      relatedRole=object_role_data['FAILSAFE']
    if object_role[80]==object_role[80]:
      occupation=information_object_data[object_role[80]]
    else:
      occupation=information_object_data['FAILSAFE']
    if object_role[81]==object_role[81]:
      occupation1=information_object_data[object_role[81]]
    else:
      occupation1=information_object_data['FAILSAFE']
    if object_role[82]==object_role[82]:
      socioEconomicDescriptor=information_object_data[object_role[82]]
    else:
      socioEconomicDescriptor=information_object_data['FAILSAFE']
    if object_role[83]==object_role[83]:
      genderIdentity=information_object_data[object_role[83]]
    else:
      genderIdentity=information_object_data['FAILSAFE']
    if object_role[85]==object_role[85]:
      objectRole20=object_role_data[object_role[85]]
    else:
      objectRole20=object_role_data['FAILSAFE']
    if object_role[86]==object_role[86]:
      objectRole21=object_role_data[object_role[86]]
    else:
      objectRole21=object_role_data['FAILSAFE']
    if object_role[87]==object_role[87]:
      objectRole22=object_role_data[object_role[87]]
    else:
      objectRole22=object_role_data['FAILSAFE']
    if object_role[88]==object_role[88]:
      objectRole23=object_role_data[object_role[88]]
    else:
      objectRole23=object_role_data['FAILSAFE']
    if object_role[89]==object_role[89]:
      objectRole24=object_role_data[object_role[89]]
    else:
      objectRole24=object_role_data['FAILSAFE']
    if object_role[90]==object_role[90]:
      objectRole25=object_role_data[object_role[90]]
    else:
      objectRole25=object_role_data['FAILSAFE']
    if object_role[91]==object_role[91]:
      objectRole26=object_role_data[object_role[91]]
    else:
      objectRole26=object_role_data['FAILSAFE']
    if object_role[92]==object_role[92]:
      objectRole27=object_role_data[object_role[92]]
    else:
      objectRole27=object_role_data['FAILSAFE']
    if object_role[93]==object_role[93]:
      objectRole28=object_role_data[object_role[93]]
    else:
      objectRole28=object_role_data['FAILSAFE']
    if object_role[94]==object_role[94]:
      objectRole29=object_role_data[object_role[94]]
    else:
      objectRole29=object_role_data['FAILSAFE']
    if object_role[95]==object_role[95]:
      objectRole30=object_role_data[object_role[95]]
    else:
      objectRole30=object_role_data['FAILSAFE']
    if object_role[96]==object_role[96]:
      objectRole31=object_role_data[object_role[96]]
    else:
      objectRole31=object_role_data['FAILSAFE']
    if object_role[97]==object_role[97]:
      objectRole32=object_role_data[object_role[97]]
    else:
      objectRole32=object_role_data['FAILSAFE']
    if object_role[98]==object_role[98]:
      objectRole33=object_role_data[object_role[98]]
    else:
      objectRole33=object_role_data['FAILSAFE']
    if object_role[99]==object_role[99]:
      objectRole34=object_role_data[object_role[99]]
    else:
      objectRole34=object_role_data['FAILSAFE']
    if object_role[100]==object_role[100]:
      objectRole35=object_role_data[object_role[100]]
    else:
      objectRole35=object_role_data['FAILSAFE']
    if object_role[101]==object_role[101]:
      objectRole36=object_role_data[object_role[101]]
    else:
      objectRole36=object_role_data['FAILSAFE']
    if object_role[102]==object_role[102]:
      objectRole37=object_role_data[object_role[102]]
    else:
      objectRole37=object_role_data['FAILSAFE']
    if object_role[103]==object_role[103]:
      objectRole38=object_role_data[object_role[103]]
    else:
      objectRole38=object_role_data['FAILSAFE']
    if object_role[104]==object_role[104]:
      objectRole39=object_role_data[object_role[104]]
    else:
      objectRole39=object_role_data['FAILSAFE']
    if object_role[120]==object_role[120]:
      factor=object_role_data[object_role[120]]
    else:
      factor=object_role_data['FAILSAFE']
    if object_role[121]==object_role[121]:
      factor1=object_role_data[object_role[121]]
    else:
      factor1=object_role_data['FAILSAFE']
    if object_role[122]==object_role[122]:
      factor2=object_role_data[object_role[122]]
    else:
      factor2=object_role_data['FAILSAFE']
    if object_role[123]==object_role[123]:
      factor3=object_role_data[object_role[123]]
    else:
      factor3=object_role_data['FAILSAFE']
    if object_role[124]==object_role[124]:
      factor4=object_role_data[object_role[124]]
    else:
      factor4=object_role_data['FAILSAFE']
    if object_role[125]==object_role[125]:
      factor5=object_role_data[object_role[125]]
    else:
      factor5=object_role_data['FAILSAFE']
    if object_role[126]==object_role[126]:
      factor6=object_role_data[object_role[126]]
    else:
      factor6=object_role_data['FAILSAFE']
    if object_role[127]==object_role[127]:
      factor7=object_role_data[object_role[127]]
    else:
      factor7=object_role_data['FAILSAFE']
    if object_role[128]==object_role[128]:
      commodity=object_role_data[object_role[128]]
    else:
      commodity=object_role_data['FAILSAFE']
    if object_role[129]==object_role[129]:
      commodity1=object_role_data[object_role[129]]
    else:
      commodity1=object_role_data['FAILSAFE']
    if object_role[130]==object_role[130]:
      commodity2=object_role_data[object_role[130]]
    else:
      commodity2=object_role_data['FAILSAFE']
    if object_role[131]==object_role[131]:
      commodity3=object_role_data[object_role[131]]
    else:
      commodity3=object_role_data['FAILSAFE']
    if object_role[132]==object_role[132]:
      commodity4=object_role_data[object_role[132]]
    else:
      commodity4=object_role_data['FAILSAFE']
    if object_role[133]==object_role[133]:
      commodity5=object_role_data[object_role[133]]
    else:
      commodity5=object_role_data['FAILSAFE']
    if object_role[134]==object_role[134]:
      commodity6=object_role_data[object_role[134]]
    else:
      commodity6=object_role_data['FAILSAFE']
    if object_role[135]==object_role[135]:
      commodity7=object_role_data[object_role[135]]
    else:
      commodity7=object_role_data['FAILSAFE']
    if object_role[136]==object_role[136]:
      commodity8=object_role_data[object_role[136]]
    else:
      commodity8=object_role_data['FAILSAFE']
    if object_role[137]==object_role[137]:
      commodity9=object_role_data[object_role[137]]
    else:
      commodity9=object_role_data['FAILSAFE']
    if object_role[138]==object_role[138]:
      commodity10=object_role_data[object_role[138]]
    else:
      commodity10=object_role_data['FAILSAFE']
    if object_role[139]==object_role[139]:
      commodity11=object_role_data[object_role[139]]
    else:
      commodity11=object_role_data['FAILSAFE']
    if object_role[140]==object_role[140]:
      commodity12=object_role_data[object_role[140]]
    else:
      commodity12=object_role_data['FAILSAFE']
    if object_role[141]==object_role[141]:
      commodity13=object_role_data[object_role[141]]
    else:
      commodity13=object_role_data['FAILSAFE']
    if object_role[142]==object_role[142]:
      commodity14=object_role_data[object_role[142]]
    else:
      commodity14=object_role_data['FAILSAFE']
    if object_role[143]==object_role[143]:
      commodity15=object_role_data[object_role[143]]
    else:
      commodity15=object_role_data['FAILSAFE']
    if object_role[144]==object_role[144]:
      commodity16=object_role_data[object_role[144]]
    else:
      commodity16=object_role_data['FAILSAFE']
    if object_role[145]==object_role[145]:
      commodity17=object_role_data[object_role[145]]
    else:
      commodity17=object_role_data['FAILSAFE']
    if object_role[146]==object_role[146]:
      commodity18=object_role_data[object_role[146]]
    else:
      commodity18=object_role_data['FAILSAFE']
    if object_role[147]==object_role[147]:
      commodity19=object_role_data[object_role[147]]
    else:
      commodity19=object_role_data['FAILSAFE']
    if object_role[148]==object_role[148]:
      commodity20=object_role_data[object_role[148]]
    else:
      commodity20=object_role_data['FAILSAFE']
    if object_role[149]==object_role[149]:
      commodity21=object_role_data[object_role[149]]
    else:
      commodity21=object_role_data['FAILSAFE']
    if object_role[150]==object_role[150]:
      commodity22=object_role_data[object_role[150]]
    else:
      commodity22=object_role_data['FAILSAFE']
    if object_role[151]==object_role[151]:
      commodity23=object_role_data[object_role[151]]
    else:
      commodity23=object_role_data['FAILSAFE']
    if object_role[152]==object_role[152]:
      commodity24=object_role_data[object_role[152]]
    else:
      commodity24=object_role_data['FAILSAFE']
    if object_role[153]==object_role[153]:
      commodity25=object_role_data[object_role[153]]
    else:
      commodity25=object_role_data['FAILSAFE']
    if object_role[154]==object_role[154]:
      sameEntity=object_role_data[object_role[154]]
    else:
      sameEntity=object_role_data['FAILSAFE']
    if object_role[155]==object_role[155]:
      sameEntity1=object_role_data[object_role[155]]
    else:
      sameEntity1=object_role_data['FAILSAFE']
    if object_role[156]==object_role[156]:
      sameEntity2=object_role_data[object_role[156]]
    else:
      sameEntity2=object_role_data['FAILSAFE'] 
    if object_role[157]==object_role[157]:
       factor8=event_role_data[object_role[157]]
    else:
       factor8=event_role_data['FAILSAFE']
    if object_role[158]==object_role[158]:
       factor9=event_role_data[object_role[158]]
    else:
       factor9=event_role_data['FAILSAFE']
    if object_role[159]==object_role[159]:
       factor10=event_role_data[[object_role[159]]
    else:
       factor10=event_role_data['FAILSAFE']
    
    return render_template("objectrole.html",
    label=object_role[2],
    
    type1L=type1[2],
    type2L=type2[2],
    type3L=type3[2],
    type4L=type4[2],
    type5L=type5[2],
    type6L=type6[2],
    type7L=type7[2],
    type8L=type8[2],
    type9L=type9[2],
    type10L=type10[2],
    type11L=type11[2],
    type12L=type12[2],
    type13L=type13[2],
    eventL=event[2],
    event1L=event1[2],
    event2L=event2[2],
    event3L=event3[2],
    event4L=event4[2],
    event5L=event5[2],
    event6L=event6[2],
    event7L=event7[2],
    event8L=event8[2],
    event9L=event9[2],
    event10L=event10[2],
    event11L=event11[2],
    event12L=event12[2],
    event13L=event13[2],
    event14L=event14[2],
    event15L=event15[2],
    event16L=event16[2],
    event17L=event17[2],
    event18L=event18[2],
    event19L=event19[2],
    objectL=object[2],
    object1L=object1[2],
    object2L=object2[2],
    object3L=object3[2],
    objectRoleL=objectRole[2],
    objectRole1L=objectRole1[2],
    objectRole2L=objectRole2[2],
    objectRole3L=objectRole3[2],
    objectRole4L=objectRole4[2],
    objectRole5L=objectRole5[2],
    objectRole6L=objectRole6[2],
    objectRole7L=objectRole7[2],
    objectRole8L=objectRole8[2],
    objectRole9L=objectRole9[2],
    objectRole10L=objectRole10[2],
    objectRole11L=objectRole11[2],
    objectRole12L=objectRole12[2],
    objectRole13L=objectRole13[2],
    objectRole14L=objectRole14[2],
    objectRole15L=objectRole15[2],
    objectRole16L=objectRole16[2],
    objectRole17L=objectRole17[2],
    objectRole18L=objectRole18[2],
    objectRole19L=objectRole19[2],
    relatedRoleL=relatedRole[2],
    occupationL= occupation[2],
    occupation1L=occupation1[2],
    socioEconomicDescriptorL=socioEconomicDescriptor[2],
    genderIdentityL=genderIdentity[2],
    approximateAgeInYears=object_role[84],
    objectRole20L=objectRole20[2],
    objectRole21L=objectRole21[2],
    objectRole22L=objectRole22[2],
    objectRole23L=objectRole23[2],
    objectRole24L=objectRole24[2],
    objectRole25L=objectRole25[2],
    objectRole26L=objectRole26[2],
    objectRole27L=objectRole27[2],
    objectRole28L=objectRole28[2],
    objectRole29L=objectRole29[2],
    objectRole30L=objectRole30[2],
    objectRole31L=objectRole31[2],
    objectRole32L=objectRole32[2],
    objectRole33L=objectRole33[2],
    objectRole34L=objectRole34[2],
    objectRole35L=objectRole35[2],
    objectRole36L=objectRole36[2],
    objectRole37L=objectRole37[2],
    objectRole38L=objectRole38[2],
    objectRole39L=objectRole39[2],
    factorL=factor[2],
    factor1L=factor1[2],
    factor2L=factor2[2],
    factor3L=factor3[2],
    factor4L=factor4[2],
    factor5L=factor5[2],
    factor6L=factor6[2],
    factor7L=factor7[2],
    commodityL=commodity[2],
    commodity1L=commodity1[2],
    commodity2L=commodity2[2],
    commodity3L=commodity3[2],
    commodity4L=commodity4[2],
    commodity5L=commodity5[2],
    commodity6L=commodity6[2],
    commodity7L=commodity7[2],
    commodity8L=commodity8[2],
    commodity9L=commodity9[2],
    commodity10L=commodity10[2],
    commodity11L=commodity11[2],
    commodity12L=commodity12[2],
    commodity13L=commodity13[2],
    commodity14L=commodity14[2],
    commodity15L=commodity15[2],
    commodity16L=commodity16[2],
    commodity17L=commodity17[2],
    commodity18L=commodity18[2],
    commodity19L=commodity19[2],
    commodity20L=commodity20[2],
    commodity21L=commodity21[2],
    commodity22L=commodity22[2],
    commodity23L=commodity23[2],
    commodity24L=commodity24[2],
    commodity25L=commodity25[2],
    sameEntityL=sameEntity[2],
    sameEntity1L=sameEntity1[2],
    sameEntity2L=sameEntity2[2],
    factor8L=factor8[2],
    factor9L=factor9[2],
    factor10L=factor10[2],
    
    type1_link='/term/'+type1[1]+'.html',
    type2_link='/term/'+type2[1]+'.html',
    type3_link='/term/'+type3[1]+'.html',
    type4_link='/term/'+type4[1]+'.html',
    type5_link='/term/'+type5[1]+'.html',
    type6_link='/term/'+type6[1]+'.html',
    type7_link='/term/'+type7[1]+'.html',
    type8_link='/term/'+type8[1]+'.html',
    type9_link='/term/'+type9[1]+'.html',
    type10_link='/term/'+type10[1]+'.html',
    type11_link='/term/'+type11[1]+'.html',
    type12_link='/term/'+type12[1]+'.html',
    type13_link='/term/'+type13[1]+'.html',
    event_link='/event/'+event[1]+'.html',
    event1_link='/event/'+event1[1]+'.html',
    event2_link='/event/'+event2[1]+'.html',
    event3_link='/event/'+event3[1]+'.html',
    event4_link='/event/'+event4[1]+'.html',
    event5_link='/event/'+event5[1]+'.html',
    event6_link='/event/'+event6[1]+'.html',
    event7_link='/event/'+event7[1]+'.html',
    event8_link='/event/'+event8[1]+'.html',
    event9_link='/event/'+event9[1]+'.html',
    event10_link='/event/'+event10[1]+'.html',
    event11_link='/event/'+event11[1]+'.html',
    event12_link='/event/'+event12[1]+'.html',
    event13_link='/event/'+event13[1]+'.html',
    event14_link='/event/'+event14[1]+'.html',
    event15_link='/event/'+event15[1]+'.html',
    event16_link='/event/'+event16[1]+'.html',
    event17_link='/event/'+event17[1]+'.html',
    event18_link='/event/'+event18[1]+'.html',
    event19_link='/event/'+event19[1]+'.html',
    object_link='/object/'+object[1]+'.html',
    object1_link='/object/'+object1[1]+'.html',
    object2_link='/object/'+object2[1]+'.html',
    object3_link='/object/'+object3[1]+'.html',
    objectRole_link='/objectrole/'+objectRole[1]+'.html',
    objectRole1_link='/objectrole/'+objectRole1[1]+'.html',
    objectRole2_link='/objectrole/'+objectRole2[1]+'.html',
    objectRole3_link='/objectrole/'+objectRole3[1]+'.html',
    objectRole4_link='/objectrole/'+objectRole4[1]+'.html',
    objectRole5_link='/objectrole/'+objectRole5[1]+'.html',
    objectRole6_link='/objectrole/'+objectRole6[1]+'.html',
    objectRole7_link='/objectrole/'+objectRole7[1]+'.html',
    objectRole8_link='/objectrole/'+objectRole8[1]+'.html',
    objectRole9_link='/objectrole/'+objectRole9[1]+'.html',
    objectRole10_link='/objectrole/'+objectRole10[1]+'.html',
    objectRole11_link='/objectrole/'+objectRole11[1]+'.html',
    objectRole12_link='/objectrole/'+objectRole12[1]+'.html',
    objectRole13_link='/objectrole/'+objectRole13[1]+'.html',
    objectRole14_link='/objectrole/'+objectRole14[1]+'.html',
    objectRole15_link='/objectrole/'+objectRole15[1]+'.html',
    objectRole16_link='/objectrole/'+objectRole16[1]+'.html',
    objectRole17_link='/objectrole/'+objectRole17[1]+'.html',
    objectRole18_link='/objectrole/'+objectRole18[1]+'.html',
    objectRole19_link='/objectrole/'+objectRole19[1]+'.html',
    relatedRole_link='/objectrole/'+relatedRole[1]+'.html',
    occupation_link='/informationobject/'+occupation[1]+'.html',
    occupation1_link='/informationobject/'+occupation1[1]+'.html',
    socioEconomicDescriptor_link='/informationobject/'+socioEconomicDescriptor[1]+'.html',
    genderIdentity_link='/informationobject/'+genderIdentity[1]+'.html',
    objectRole20_link='/objectrole/'+objectRole20[1]+'.html',
    objectRole21_link='/objectrole/'+objectRole21[1]+'.html',
    objectRole22_link='/objectrole/'+objectRole22[1]+'.html',
    objectRole23_link='/objectrole/'+objectRole23[1]+'.html',
    objectRole24_link='/objectrole/'+objectRole24[1]+'.html',
    objectRole25_link='/objectrole/'+objectRole25[1]+'.html',
    objectRole26_link='/objectrole/'+objectRole26[1]+'.html',
    objectRole27_link='/objectrole/'+objectRole27[1]+'.html',
    objectRole28_link='/objectrole/'+objectRole28[1]+'.html',
    objectRole29_link='/objectrole/'+objectRole29[1]+'.html',
    objectRole30_link='/objectrole/'+objectRole30[1]+'.html',
    objectRole31_link='/objectrole/'+objectRole31[1]+'.html',
    objectRole32_link='/objectrole/'+objectRole32[1]+'.html',
    objectRole33_link='/objectrole/'+objectRole33[1]+'.html',
    objectRole34_link='/objectrole/'+objectRole34[1]+'.html',
    objectRole35_link='/objectrole/'+objectRole35[1]+'.html',
    objectRole36_link='/objectrole/'+objectRole36[1]+'.html',
    objectRole37_link='/objectrole/'+objectRole37[1]+'.html',
    objectRole38_link='/objectrole/'+objectRole38[1]+'.html',
    objectRole39_link='/objectrole/'+objectRole39[1]+'.html',
    factor_link='/objectrole/'+factor[1]+'.html',
    factor1_link='/objectrole/'+factor1[1]+'.html',
    factor2_link='/objectrole/'+factor2[1]+'.html',
    factor3_link='/objectrole/'+factor3[1]+'.html',
    factor4_link='/objectrole/'+factor4[1]+'.html',
    factor5_link='/objectrole/'+factor5[1]+'.html',
    factor6_link='/objectrole/'+factor6[1]+'.html',
    factor7_link='/objectrole/'+factor7[1]+'.html',
    commodity_link='/objectrole/'+commodity[1]+'.html',
    commodity1_link='/objectrole/'+commodity1[1]+'.html',
    commodity2_link='/objectrole/'+commodity2[1]+'.html',
    commodity3_link='/objectrole/'+commodity3[1]+'.html',
    commodity4_link='/objectrole/'+commodity4[1]+'.html',
    commodity5_link='/objectrole/'+commodity5[1]+'.html',
    commodity6_link='/objectrole/'+commodity6[1]+'.html',
    commodity7_link='/objectrole/'+commodity7[1]+'.html',
    commodity8_link='/objectrole/'+commodity8[1]+'.html',
    commodity9_link='/objectrole/'+commodity9[1]+'.html',
    commodity10_link='/objectrole/'+commodity10[1]+'.html',
    commodity11_link='/objectrole/'+commodity11[1]+'.html',
    commodity12_link='/objectrole/'+commodity12[1]+'.html',
    commodity13_link='/objectrole/'+commodity13[1]+'.html',
    commodity14_link='/objectrole/'+commodity14[1]+'.html',
    commodity15_link='/objectrole/'+commodity15[1]+'.html',
    commodity16_link='/objectrole/'+commodity16[1]+'.html',
    commodity17_link='/objectrole/'+commodity17[1]+'.html',
    commodity18_link='/objectrole/'+commodity18[1]+'.html',
    commodity19_link='/objectrole/'+commodity19[1]+'.html',
    commodity20_link='/objectrole/'+commodity20[1]+'.html',
    commodity21_link='/objectrole/'+commodity21[1]+'.html',
    commodity22_link='/objectrole/'+commodity22[1]+'.html',
    commodity23_link='/objectrole/'+commodity23[1]+'.html',
    commodity24_link='/objectrole/'+commodity24[1]+'.html',
    commodity25_link='/objectrole/'+commodity25[1]+'.html',
    sameEntity_link='/objectrole/'+sameEntity[1]+'.html',
    sameEntity1_link='/objectrole/'+sameEntity1[1]+'.html',
    sameEntity2_link='/objectrole/'+sameEntity2[1]+'.html',
    factor8_link='/eventrole/'+factor8[1]+'.html',
    factor9_link='/eventrole/'+factor9[1]+'.html',
    factor10_link='/eventrole/'+factor10[1]+'.html',
   )

@app.route("/eventrole/<IRI>.html")   
def eventrole(IRI):
    event_role = event_role_data[IRI]
    type1=term_data[event_role[3]]
    type2=term_data[event_role[4]]
    type3=term_data[event_role[5]]
    type4=term_data[event_role[6]]
    type5=term_data[event_role[7]]
    if event_role[8]==event_role[8]:
      type6=term_data[event_role[8]]
    else:
      type6=term_data['FAILSAFE']
    if event_role[9]==event_role[9]:
      type7=term_data[event_role[9]]
    else:
      type7=term_data['FAILSAFE']
    if event_role[10]==event_role[10]:
      type8=term_data[event_role[10]]
    else:
      type8=term_data['FAILSAFE']
    event=event_data[event_role[11]]
    if event_role[12]==event_role[12]:
      event1=event_data[event_role[12]]
    else:
      event1=event_data['FAILSAFE']
    if event_role[13]==event_role[13]:
      event2=event_data[event_role[13]]
    else:
      event2=event_data['FAILSAFE']
    if event_role[14]==event_role[14]:
      decisionMaker=object_role_data[event_role[14]]
    else:
      decisionMaker=object_role_data['FAILSAFE']
    if event_role[15]==event_role[15]:
      decisionMaker1=object_role_data[event_role[15]]
    else:
      decisionMaker1=object_role_data['FAILSAFE']
    if event_role[16]==event_role[16]:
      decisionMaker2=object_role_data[event_role[16]]
    else:
      decisionMaker2=object_role_data['FAILSAFE']
    if event_role[17]==event_role[17]:
      decisionMaker3=object_role_data[event_role[17]]
    else:
      decisionMaker3=object_role_data['FAILSAFE']
    if event_role[18]==event_role[18]:
      decisionMaker4=object_role_data[event_role[18]]
    else:
      decisionMaker4=object_role_data['FAILSAFE']
    if event_role[19]==event_role[19]:
      decisionMaker5=object_role_data[event_role[19]]
    else:
      decisionMaker5=object_role_data['FAILSAFE']
    if event_role[20]==event_role[20]:
      decisionMaker6=object_role_data[event_role[20]]
    else:
      decisionMaker6=object_role_data['FAILSAFE']
    if event_role[21]==event_role[21]:
      decisionMaker7=object_role_data[event_role[21]]
    else:
      decisionMaker7=object_role_data['FAILSAFE']
    if event_role[22]==event_role[22]:
      decisionMaker8=object_role_data[event_role[22]]
    else:
      decisionMaker8=object_role_data['FAILSAFE']
    if event_role[23]==event_role[23]:
      decisionMaker9=object_role_data[event_role[23]]
    else:
      decisionMaker9=object_role_data['FAILSAFE']
    if event_role[24]==event_role[24]:
      decisionMaker10=object_role_data[event_role[24]]
    else:
      decisionMaker10=object_role_data['FAILSAFE']
    if event_role[25]==event_role[25]:
      decisionMaker11=object_role_data[event_role[25]]
    else:
      decisionMaker11=object_role_data['FAILSAFE']
    if event_role[26]==event_role[26]:
      decisionMaker12=object_role_data[event_role[26]]
    else:
      decisionMaker12=object_role_data['FAILSAFE']
    if event_role[27]==event_role[27]:
      decisionMaker13=object_role_data[event_role[27]]
    else:
      decisionMaker13=object_role_data['FAILSAFE']
    if event_role[28]==event_role[28]:
      decisionMaker14=object_role_data[event_role[28]]
    else:
      decisionMaker14=object_role_data['FAILSAFE']
    if event_role[29]==event_role[29]:
      decisionMaker15=object_role_data[event_role[29]]
    else:
      decisionMaker15=object_role_data['FAILSAFE']
    if event_role[30]==event_role[30]:
      decisionMaker16=object_role_data[event_role[30]]
    else:
      decisionMaker16=object_role_data['FAILSAFE']
    if event_role[31]==event_role[31]:
      decisionMaker17=object_role_data[event_role[31]]
    else:
      decisionMaker17=object_role_data['FAILSAFE']
    if event_role[32]==event_role[32]:
      decisionMaker18=object_role_data[event_role[32]]
    else:
      decisionMaker18=object_role_data['FAILSAFE']
    if event_role[33]==event_role[33]:
      decisionMaker19=object_role_data[event_role[33]]
    else:
      decisionMaker19=object_role_data['FAILSAFE']
    if event_role[44]==event_role[44]:
      sameEntity=event_role_data[event_role[44]]
    else:
      sameEntity=object_role_data['FAILSAFE']
    return render_template("eventrole.html",
    label=event_role[2],
    
    type1L=type1[2],
    type2L=type2[2],
    type3L=type3[2],
    type4L=type4[2],
    type5L=type5[2],
    type6L=type6[2],
    type7L=type7[2],
    type8L=type8[2],
    eventL=event[2],
    event1L=event1[2],
    event2L=event2[2],
    decisionMakerL=decisionMaker[2],
    decisionMaker1L=decisionMaker1[2],
    decisionMaker2L=decisionMaker2[2],
    decisionMaker3L=decisionMaker3[2],
    decisionMaker4L=decisionMaker4[2],
    decisionMaker5L=decisionMaker5[2],
    decisionMaker6L=decisionMaker6[2],
    decisionMaker7L=decisionMaker7[2],
    decisionMaker8L=decisionMaker8[2],
    decisionMaker9L=decisionMaker9[2],
    decisionMaker10L=decisionMaker10[2],
    decisionMaker11L=decisionMaker11[2],
    decisionMaker12L=decisionMaker12[2],
    decisionMaker13L=decisionMaker13[2],
    decisionMaker14L=decisionMaker14[2],
    decisionMaker15L=decisionMaker15[2],
    decisionMaker16L=decisionMaker16[2],
    decisionMaker17L=decisionMaker17[2],
    decisionMaker18L=decisionMaker18[2],
    decisionMaker19L=decisionMaker19[2],
    sameEntityL=sameEntity[2],

    type1_link='/term/'+type1[1]+'.html',
    type2_link='/term/'+type2[1]+'.html',
    type3_link='/term/'+type3[1]+'.html',
    type4_link='/term/'+type4[1]+'.html',
    type5_link='/term/'+type5[1]+'.html',
    type6_link='/term/'+type6[1]+'.html',
    type7_link='/term/'+type7[1]+'.html',
    type8_link='/term/'+type8[1]+'.html',
    event_link='/event/'+event[1]+'.html',
    event1_link='/event/'+event1[1]+'.html',
    event2_link='/event/'+event2[1]+'.html',
    decisionMaker_link='/objectrole/'+decisionMaker[1]+'.html',
    decisionMaker1_link='/objectrole/'+decisionMaker1[1]+'.html',
    decisionMaker2_link='/objectrole/'+decisionMaker2[1]+'.html',
    decisionMaker3_link='/objectrole/'+decisionMaker3[1]+'.html',
    decisionMaker4_link='/objectrole/'+decisionMaker4[1]+'.html',
    decisionMaker5_link='/objectrole/'+decisionMaker5[1]+'.html',
    decisionMaker6_link='/objectrole/'+decisionMaker6[1]+'.html',
    decisionMaker7_link='/objectrole/'+decisionMaker7[1]+'.html',
    decisionMaker8_link='/objectrole/'+decisionMaker8[1]+'.html',
    decisionMaker9_link='/objectrole/'+decisionMaker9[1]+'.html',
    decisionMaker10_link='/objectrole/'+decisionMaker10[1]+'.html',
    decisionMaker11_link='/objectrole/'+decisionMaker11[1]+'.html',
    decisionMaker12_link='/objectrole/'+decisionMaker12[1]+'.html',
    decisionMaker13_link='/objectrole/'+decisionMaker13[1]+'.html',
    decisionMaker14_link='/objectrole/'+decisionMaker14[1]+'.html',
    decisionMaker15_link='/objectrole/'+decisionMaker15[1]+'.html',
    decisionMaker16_link='/objectrole/'+decisionMaker16[1]+'.html',
    decisionMaker17_link='/objectrole/'+decisionMaker17[1]+'.html',
    decisionMaker18_link='/objectrole/'+decisionMaker18[1]+'.html',
    decisionMaker19_link='/objectrole/'+decisionMaker19[1]+'.html',
    sameEntity_link='/eventrole/'+sameEntity[1]+'.html',
   )
    
@app.route("/event/<IRI>.html")
def event(IRI):
    event=event_data[IRI]
    type1=term_data[event[3]]
    if event[4]==event[4]:
      type2=term_data[event[4]]
    else:
      type2=term_data['FAILSAFE']
    if event[5]==event[5]:
      type3=term_data[event[5]]
    else:
      type3=term_data['FAILSAFE']
    if event[6]==event[6]:
      type4=term_data[event[6]]
    else:
      type4=term_data['FAILSAFE']
    if event[7]==event[7]:
      type5=term_data[event[7]]
    else:
      type5=term_data['FAILSAFE']
    if event[8]==event[8]:
      type6=term_data[event[8]]
    else:
      type6=term_data['FAILSAFE']
    if event[9]==event[9]:
      type7=term_data[event[9]]
    else:
      type7=term_data['FAILSAFE']
    if event[10]==event[10]:
      type8=term_data[event[10]]
    else:
      type8=term_data['FAILSAFE']
    if event[11]==event[11]:
      type9=term_data[event[11]]
    else:
      type9=term_data['FAILSAFE']
    if event[12]==event[12]:
      type10=term_data[event[12]]
    else:
      type10=term_data['FAILSAFE']
    if event[13]==event[13]:
      type11=term_data[event[13]]
    else:
      type11=term_data['FAILSAFE']
    if event[14]==event[14]:
      event0=event_data[event[14]]
    else:
      event0=event_data['FAILSAFE']
    if event[15]==event[15]:
      event1=event_data[event[15]]
    else:
      event1=event_data['FAILSAFE']
    if event[16]==event[16]:
      event2=event_data[event[16]]
    else:
      event2=event_data['FAILSAFE']
    if event[23]==event[23]:
      record=record_data[event[23]]
    else:
      record=record_data['FAILSAFE']
    if event[24]==event[24]:
      eventRole=event_role_data[event[24]]
    else:
      eventRole=event_role_data['FAILSAFE']
    if event[26]==event[26]:
      objectRole=object_role_data[event[26]]
    else:
      objectRole=object_role_data['FAILSAFE']
    if event[27]==event[27]:
      objectRole1=object_role_data[event[27]]
    else:
      objectRole1=object_role_data['FAILSAFE']
    if event[28]==event[28]:
      objectRole2=object_role_data[event[28]]
    else:
      objectRole2=object_role_data['FAILSAFE']
    if event[29]==event[29]:
      objectRole3=object_role_data[event[29]]
    else:
      objectRole3=object_role_data['FAILSAFE']
    if event[30]==event[30]:
      objectRole4=object_role_data[event[30]]
    else:
      objectRole4=object_role_data['FAILSAFE']
    if event[31]==event[31]:
      objectRole5=object_role_data[event[31]]
    else:
      objectRole5=object_role_data['FAILSAFE']
    if event[32]==event[32]:
      objectRole6=object_role_data[event[32]]
    else:
      objectRole6=event_data['FAILSAFE']
    if event[33]==event[33]:
      objectRole7=object_role_data[event[33]]
    else:
      objectRole7=object_role_data['FAILSAFE']
    if event[34]==event[34]:
      objectRole8=object_role_data[event[34]]
    else:
      objectRole8=object_role_data['FAILSAFE']
    if event[35]==event[35]:
      objectRole9=object_role_data[event[35]]
    else:
      objectRole9=object_role_data['FAILSAFE']
    if event[36]==event[36]:
      objectRole10=object_role_data[event[36]]
    else:
      objectRole10=object_role_data['FAILSAFE']
    if event[37]==event[37]:
      objectRole11=object_role_data[event[37]]
    else:
      objectRole11=object_role_data['FAILSAFE']
    if event[38]==event[38]:
      objectRole12=object_role_data[event[38]]
    else:
      objectRole12=object_role_data['FAILSAFE']
    if event[39]==event[39]:
      objectRole13=object_role_data[event[39]]
    else:
      objectRole13=object_role_data['FAILSAFE']
    if event[40]==event[40]:
      objectRole14=object_role_data[event[40]]
    else:
      objectRole14=object_role_data['FAILSAFE']
    if event[41]==event[41]:
      objectRole15=object_role_data[event[41]]
    else:
      objectRole15=object_role_data['FAILSAFE']
    if event[42]==event[42]:
      objectRole16=object_role_data[event[42]]
    else:
      objectRole16=object_role_data['FAILSAFE']
    if event[43]==event[43]:
      objectRole17=object_role_data[event[43]]
    else:
      objectRole17=object_role_data['FAILSAFE']
    if event[44]==event[44]:
      objectRole18=object_role_data[event[44]]
    else:
      objectRole18=object_role_data['FAILSAFE']
    if event[45]==event[45]:
      objectRole19=object_role_data[event[45]]
    else:
      objectRole19=object_role_data['FAILSAFE']
    if event[149]==event[149]:
      topic=information_object_data[event[149]]
    else:
      topic=information_object_data['FAILSAFE']
    if event[150]==event[150]:
      topic1=information_object_data[event[150]]
    else:
      topic1=information_object_data['FAILSAFE']
    if event[151]==event[151]:
      event3=event_data[event[151]]
    else:
      event3=event_data['FAILSAFE']
    if event[152]==event[152]:
      relatedEvent=event_data[event[152]]
    else:
      relatedEvent=event_data['FAILSAFE']
    if event[153]==event[153]:
      relatedEvent1=event_data[event[153]]
    else:
      relatedEvent1=event_data['FAILSAFE']
    if event[154]==event[154]:
      relatedEvent2=event_data[event[154]]
    else:
      relatedEvent2=event_data['FAILSAFE']
    if event[155]==event[155]:
      relatedEvent3=event_data[event[155]]
    else:
      relatedEvent3=event_data['FAILSAFE']
    if event[156]==event[156]:
      relatedEvent4=event_data[event[156]]
    else:
      relatedEvent4=event_data['FAILSAFE']
    if event[157]==event[157]:
      relatedEvent5=event_data[event[157]]
    else:
      relatedEvent5=event_data['FAILSAFE']
    if event[158]==event[158]:
      relatedEvent6=event_data[event[158]]
    else:
      relatedEvent6=event_data['FAILSAFE']
    if event[159]==event[159]:
      relatedEvent7=event_data[event[159]]
    else:
      relatedEvent7=event_data['FAILSAFE']
    if event[160]==event[160]:
      relatedEvent8=event_data[event[160]]
    else:
      relatedEvent8=event_data['FAILSAFE']
    if event[161]==event[161]:
      relatedEvent9=event_data[event[161]]
    else:
      relatedEvent9=event_data['FAILSAFE']
    if event[162]==event[162]:
      relatedEvent10=event_data[event[162]]
    else:
      relatedEvent10=event_data['FAILSAFE']
    if event[163]==event[163]:
      relatedEvent11=event_data[event[163]]
    else:
      relatedEvent11=event_data['FAILSAFE']
    if event[164]==event[164]:
      relatedEvent12=event_data[event[164]]
    else:
      relatedEvent12=event_data['FAILSAFE']
    if event[165]==event[165]:
      relatedEvent13=event_data[event[165]]
    else:
      relatedEvent13=event_data['FAILSAFE']
    if event[166]==event[166]:
      relatedEvent14=event_data[event[166]]
    else:
      relatedEvent14=event_data['FAILSAFE']
    if event[167]==event[167]:
      relatedEvent15=event_data[event[167]]
    else:
      relatedEvent15=event_data['FAILSAFE']
    if event[168]==event[168]:
      relatedEvent16=event_data[event[168]]
    else:
      relatedEvent16=event_data['FAILSAFE']
    if event[169]==event[169]:
      relatedEvent17=event_data[event[169]]
    else:
      relatedEvent17=event_data['FAILSAFE']
    if event[170]==event[170]:
      relatedEvent18=event_data[event[170]]
    else:
      relatedEvent18=event_data['FAILSAFE']
    if event[171]==event[171]:
      relatedEvent19=event_data[event[171]]
    else:
      relatedEvent19=event_data['FAILSAFE']
    if event[247]==event[247]:
      sameEntity=event_data[event[247]]
    else:
      sameEntity=event_role_data['FAILSAFE']
    if event[248]==event[248]:
      sameEntity1=event_data[event[248]]
    else:
      sameEntity1=event_role_data['FAILSAFE']
    if event[249]==event[249]:
       eventRole1=event_role_data[event[249]]
    else:
       eventRole1=event_role_data['FAILSAFE']
    if event[250]==event[250]:
       eventRole2=event_role_data[event[250]]
    else:
       eventRole2=event_role_data['FAILSAFE']
    if event[251]==event[251]:
       eventRole3=event_role_data[event[251]]
    else:
       eventRole3=event_role_data['FAILSAFE']
    if event[252]==event[252]:
       eventRole4=event_role_data[event[252]]
    else:
       eventRole4=event_data['FAILSAFE']
    if event[253]==event[253]:
       eventRole5=event_role_data[event[253]]
    else:
       eventRole5=event_role_data['FAILSAFE']
    if event[254]==event[254]:
       eventRole6=event_role_data[event[254]]
    else:
       eventRole6=event_role_data['FAILSAFE']
    if event[255]==event[255]:
       eventRole7=event_role_data[event[255]]
    else:
       eventRole7=event_role_data['FAILSAFE']     
      
    return render_template("event.html",
    label=event[2],
    
    type1L=type1[2],
    type2L=type2[2],
    type3L=type3[2],
    type4L=type4[2],
    type5L=type5[2],
    type6L=type6[2],
    type7L=type7[2],
    type8L=type8[2],
    type9L=type9[2],
    type10L=type10[2],
    type11L=type11[2],
    event0L=event0[2],
    event1L=event1[2],
    event2L=event2[2],
    GivenDate=event[17],
    InterpretedDate=event[18],
    PSEDate=event[19],
    ApproximateDurationInMonths=event[20],
    ApproximateNumberOfSittings=event[21],
    ApproximateSittingDurationInHours=event[22],
    recordL=record[2],
    eventRoleL=eventRole[2],
    comment=event[25],
    objectRoleL=objectRole[2],
    objectRole1L=objectRole1[2],
    objectRole2L=objectRole2[2],
    objectRole3L=objectRole3[2],
    objectRole4L=objectRole4[2],
    objectRole5L=objectRole5[2],
    objectRole6L=objectRole6[2],
    objectRole7L=objectRole7[2],
    objectRole8L=objectRole8[2],
    objectRole9L=objectRole9[2],
    objectRole10L=objectRole10[2],
    objectRole11L=objectRole11[2],
    objectRole12L=objectRole12[2],
    objectRole13L=objectRole13[2],
    objectRole14L=objectRole14[2],
    objectRole15L=objectRole15[2],
    objectRole16L=objectRole16[2],
    objectRole17L=objectRole17[2],
    objectRole18L=objectRole18[2],
    objectRole19L=objectRole19[2],
    topicL=topic[2],
    topic1L=topic1[2],
    event3L=event3[2],
    relatedEventL=relatedEvent[2],
    relatedEvent1L=relatedEvent1[2],
    relatedEvent2L=relatedEvent2[2],
    relatedEvent3L=relatedEvent3[2],
    relatedEvent4L=relatedEvent4[2],
    relatedEvent5L=relatedEvent5[2],
    relatedEvent6L=relatedEvent6[2],
    relatedEvent7L=relatedEvent7[2],
    relatedEvent8L=relatedEvent8[2],
    relatedEvent9L=relatedEvent9[2],
    relatedEvent10L=relatedEvent10[2],
    relatedEvent11L=relatedEvent11[2],
    relatedEvent12L=relatedEvent12[2],
    relatedEvent13L=relatedEvent13[2],
    relatedEvent14L=relatedEvent14[2],
    relatedEvent15L=relatedEvent15[2],
    relatedEvent16L=relatedEvent16[2],
    relatedEvent17L=relatedEvent17[2],
    relatedEvent18L=relatedEvent18[2],
    relatedEvent19L=relatedEvent19[2],
    sameEntityL=sameEntity[2],
    sameEntity1L=sameEntity1[2],
    eventRole1L=eventRole1[2],
    eventRole2L=eventRole2[2],
    eventRole3L=eventRole3[2],
    eventRole4L=eventRole4[2],
    eventRole5L=eventRole5[2],
    eventRole6L=eventRole6[2],
    eventRole7L=eventRole7[2],

    type1_link='/term/'+type1[1]+'.html',
    type2_link='/term/'+type2[1]+'.html',
    type3_link='/term/'+type3[1]+'.html',
    type4_link='/term/'+type4[1]+'.html',
    type5_link='/term/'+type5[1]+'.html',
    type6_link='/term/'+type6[1]+'.html',
    type7_link='/term/'+type7[1]+'.html',
    type8_link='/term/'+type8[1]+'.html',
    type9_link='/term/'+type9[1]+'.html',
    type10_link='/term/'+type10[1]+'.html',
    type11_link='/term/'+type11[1]+'.html',
    event_link='/event/'+event[1]+'.html',
    event1_link='/event/'+event1[1]+'.html',
    event2_link='/event/'+event2[1]+'.html',
    record_link='/record/'+record[1]+'.html',
    eventRole_link='/eventrole/'+eventRole[1]+'.html',
    objectRole_link='/objectrole/'+objectRole[1]+'.html',
    objectRole1_link='/objectrole/'+objectRole1[1]+'.html',
    objectRole2_link='/objectrole/'+objectRole2[1]+'.html',
    objectRole3_link='/objectrole/'+objectRole3[1]+'.html',
    objectRole4_link='/objectrole/'+objectRole4[1]+'.html',
    objectRole5_link='/objectrole/'+objectRole5[1]+'.html',
    objectRole6_link='/objectrole/'+objectRole6[1]+'.html',
    objectRole7_link='/objectrole/'+objectRole7[1]+'.html',
    objectRole8_link='/objectrole/'+objectRole8[1]+'.html',
    objectRole9_link='/objectrole/'+objectRole9[1]+'.html',
    objectRole10_link='/objectrole/'+objectRole10[1]+'.html',
    objectRole11_link='/objectrole/'+objectRole11[1]+'.html',
    objectRole12_link='/objectrole/'+objectRole12[1]+'.html',
    objectRole13_link='/objectrole/'+objectRole13[1]+'.html',
    objectRole14_link='/objectrole/'+objectRole14[1]+'.html',
    objectRole15_link='/objectrole/'+objectRole15[1]+'.html',
    objectRole16_link='/objectrole/'+objectRole16[1]+'.html',
    objectRole17_link='/objectrole/'+objectRole17[1]+'.html',
    objectRole18_link='/objectrole/'+objectRole18[1]+'.html',
    objectRole19_link='/objectrole/'+objectRole19[1]+'.html',
    topic_link='/objectrole/'+topic[1]+'.html',
    topic1_link='/objectrole/'+topic1[1]+'.html',
    event3_link='/event/'+event3[1]+'.html',
    relatedEvent_link='/event/'+relatedEvent[1]+'.html',
    relatedEvent1_link='/event/'+relatedEvent1[1]+'.html',
    relatedEvent2_link='/event/'+relatedEvent2[1]+'.html',
    relatedEvent3_link='/event/'+relatedEvent3[1]+'.html',
    relatedEvent4_link='/event/'+relatedEvent4[1]+'.html',
    relatedEvent5_link='/event/'+relatedEvent5[1]+'.html',
    relatedEvent6_link='/event/'+relatedEvent6[1]+'.html',
    relatedEvent7_link='/event/'+relatedEvent7[1]+'.html',
    relatedEvent8_link='/event/'+relatedEvent8[1]+'.html',
    relatedEvent9_link='/event/'+relatedEvent9[1]+'.html',
    relatedEvent10_link='/event/'+relatedEvent10[1]+'.html',
    relatedEvent11_link='/event/'+relatedEvent11[1]+'.html',
    relatedEvent12_link='/event/'+relatedEvent12[1]+'.html',
    relatedEvent13_link='/event/'+relatedEvent13[1]+'.html',
    relatedEvent14_link='/event/'+relatedEvent14[1]+'.html',
    relatedEvent15_link='/event/'+relatedEvent15[1]+'.html',
    relatedEvent16_link='/event/'+relatedEvent16[1]+'.html',
    relatedEvent17_link='/event/'+relatedEvent17[1]+'.html',
    relatedEvent18_link='/event/'+relatedEvent18[1]+'.html',
    relatedEvent19_link='/event/'+relatedEvent19[1]+'.html',
    sameEntity_link='/event/'+sameEntity[1]+'.html',
    sameEntity1_link='/event/'+sameEntity1[1]+'.html',
    eventRole1_link='/eventrole/'+eventRole1[1]+'.html',
    eventRole2_link='/eventrole/'+eventRole2[1]+'.html',
    eventRole3_link='/eventrole/'+eventRole3[1]+'.html',
    eventRole4_link='/eventrole/'+eventRole4[1]+'.html',
    eventRole5_link='/eventrole/'+eventRole5[1]+'.html',
    eventRole6_link='/eventrole/'+eventRole6[1]+'.html',
    eventRole7_link='/eventrole/'+eventRole7[1]+'.html',
  )
  
@app.route("/object/<IRI>.html")   
def object(IRI):
    general_object=general_object_data[IRI]
    type1=term_data[general_object[3]]
    type2=term_data[general_object[4]]
    type3=term_data[general_object[5]]
    if general_object[6]==general_object[6]:
      type4=term_data[general_object[6]]
    else:
      type4=term_data['FAILSAFE']
    if general_object[7]==general_object[7]:
      type5=term_data[general_object[7]]
    else:
      type5=term_data['FAILSAFE']
    if general_object[8]==general_object[8]:
      type6=term_data[general_object[8]]
    else:
      type6=term_data['FAILSAFE']
    if general_object[9]==general_object[9]:
      type7=term_data[general_object[9]]
    else:
      type7=term_data['FAILSAFE']
    if general_object[11]==general_object[11]:
      unit=information_object_data[general_object[11]]
    else:
      unit=information_object_data['FAILSAFE']
    if general_object[15]==general_object[15]:
      member=general_object_data[general_object[15]]
    else:
      member=general_object_data['FAILSAFE']
    if general_object[16]==general_object[16]:
      member1=general_object_data[general_object[16]]
    else:
      member1=general_object_data['FAILSAFE']
    if general_object[17]==general_object[17]:
      member2=general_object_data[general_object[17]]
    else:
      member2=general_object_data['FAILSAFE']
    if general_object[18]==general_object[18]:
      member3=general_object_data[general_object[18]]
    else:
      member3=general_object_data['FAILSAFE']
    if general_object[19]==general_object[19]:
      member4=general_object_data[general_object[19]]
    else:
      member4=general_object_data['FAILSAFE']
    if general_object[20]==general_object[20]:
      relatedAgent=general_object_data[general_object[20]]
    else:
      relatedAgent=general_object_data['FAILSAFE']
    if general_object[21]==general_object[21]:
      space=general_object_data[general_object[21]]
    else:
      space=general_object_data['FAILSAFE']
    if general_object[22]==general_object[22]:
      space1=general_object_data[general_object[22]]
    else:
      space1=general_object_data['FAILSAFE']
    if general_object[23]==general_object[23]:
      space2=general_object_data[general_object[23]]
    else:
      space2=general_object_data['FAILSAFE']
    if general_object[24]==general_object[24]:
      space3=general_object_data[general_object[24]]
    else:
      space3=general_object_data['FAILSAFE']
    if general_object[25]==general_object[25]:
      space4=general_object_data[general_object[25]]
    else:
      space4=general_object_data['FAILSAFE']
    if general_object[26]==general_object[26]:
      space5=general_object_data[general_object[26]]
    else:
      space5=general_object_data['FAILSAFE']
    if general_object[27]==general_object[27]:
      objectRole=object_role_data[general_object[27]]
    else:
      objectRole=object_role_data['FAILSAFE']
    if general_object[28]==general_object[28]:
      objectRole1=object_role_data[general_object[28]]
    else:
      objectRole1=object_role_data['FAILSAFE']
    if general_object[29]==general_object[29]:
      objectRole2=object_role_data[general_object[29]]
    else:
      objectRole2=object_role_data['FAILSAFE']
    if general_object[30]==general_object[30]:
      objectRole3=object_role_data[general_object[30]]
    else:
      objectRole3=object_role_data['FAILSAFE']
    if general_object[31]==general_object[31]:
      objectRole4=object_role_data[general_object[31]]
    else:
      objectRole4=object_role_data['FAILSAFE']
    if general_object[32]==general_object[32]:
      objectRole5=object_role_data[general_object[32]]
    else:
      objectRole5=object_role_data['FAILSAFE']
    if general_object[33]==general_object[33]:
      objectRole6=object_role_data[general_object[33]]
    else:
      objectRole6=object_role_data['FAILSAFE']
    if general_object[34]==general_object[34]:
      objectRole7=object_role_data[general_object[34]]
    else:
      objectRole7=object_role_data['FAILSAFE']
    if general_object[35]==general_object[35]:
      objectRole8=object_role_data[general_object[35]]
    else:
      objectRole8=object_role_data['FAILSAFE']
    if general_object[36]==general_object[36]:
      objectRole9=object_role_data[general_object[36]]
    else:
      objectRole9=object_role_data['FAILSAFE']
    if general_object[37]==general_object[37]:
      objectRole10=object_role_data[general_object[37]]
    else:
      objectRole10=object_role_data['FAILSAFE']
    if general_object[38]==general_object[38]:
      objectRole11=object_role_data[general_object[38]]
    else:
      objectRole11=object_role_data['FAILSAFE']
    if general_object[39]==general_object[39]:
      objectRole12=object_role_data[general_object[39]]
    else:
      objectRole12=object_role_data['FAILSAFE']
    if general_object[40]==general_object[40]:
      objectRole13=object_role_data[general_object[40]]
    else:
      objectRole13=object_role_data['FAILSAFE']
    if general_object[41]==general_object[41]:
      objectRole14=object_role_data[general_object[41]]
    else:
      objectRole14=object_role_data['FAILSAFE']
    if general_object[42]==general_object[42]:
      objectRole15=object_role_data[general_object[42]]
    else:
      objectRole15=object_role_data['FAILSAFE']
    if general_object[43]==general_object[43]:
      objectRole16=object_role_data[general_object[43]]
    else:
      objectRole16=object_role_data['FAILSAFE']
    if general_object[44]==general_object[44]:
      objectRole17=object_role_data[general_object[44]]
    else:
      objectRole17=object_role_data['FAILSAFE']
    if general_object[45]==general_object[45]:
      objectRole18=object_role_data[general_object[45]]
    else:
      objectRole18=object_role_data['FAILSAFE']
    if general_object[46]==general_object[46]:
      objectRole19=object_role_data[general_object[46]]
    else:
      objectRole19=object_role_data['FAILSAFE']
    if general_object[84]==general_object[84]:
      sameEntity=general_object_data[general_object[84]]
    else:
      sameEntity=general_object_data['FAILSAFE']
    if general_object[85]==general_object[85]:
      sameEntity1=general_object_data[general_object[85]]
    else:
      sameEntity1=general_object_data['FAILSAFE']
    return render_template("generalobject.html",
    label=general_object[2],

    type1L=type1[2],
    type2L=type2[2],
    type3L=type3[2],
    type4L=type4[2],
    type5L=type5[2],
    type6L=type6[2],
    type7L=type7[2],
    value=general_object[10],
    unitL=unit[2],
    PSEValue=general_object[12],
    yearOfBirth=general_object[13],
    yearOfDeath=general_object[14],   
    memberL=member[2],
    member1L=member1[2],
    member2L=member2[2],
    member3L=member3[2],
    member4L=member4[2],
    relatedAgentL=relatedAgent[2],
    spaceL=space[2],
    space1L=space1[2],
    space2L=space2[2],
    space3L=space3[2],
    space4L=space4[2],
    space5L=space5[2],
    objectRoleL=objectRole[2],
    objectRole1L=objectRole1[2],
    objectRole2L=objectRole2[2],
    objectRole3L=objectRole3[2],
    objectRole4L=objectRole4[2],
    objectRole5L=objectRole5[2],
    objectRole6L=objectRole6[2],
    objectRole7L=objectRole7[2],
    objectRole8L=objectRole8[2],
    objectRole9L=objectRole9[2],
    objectRole10L=objectRole10[2],
    objectRole11L=objectRole11[2],
    objectRole12L=objectRole12[2],
    objectRole13L=objectRole13[2],
    objectRole14L=objectRole14[2],
    objectRole15L=objectRole15[2],
    objectRole16L=objectRole16[2],
    objectRole17L=objectRole17[2],
    objectRole18L=objectRole18[2],
    objectRole19L=objectRole19[2],
    link=general_object[82],
    link1=general_object[83],
    sameEntityL=sameEntity[2],
    sameEntity1L=sameEntity1[2],

    type1_link='/term/'+type1[1]+'.html',
    type2_link='/term/'+type2[1]+'.html',
    type3_link='/term/'+type3[1]+'.html',
    type4_link='/term/'+type4[1]+'.html',
    type5_link='/term/'+type5[1]+'.html',
    type6_link='/term/'+type6[1]+'.html',
    type7_link='/term/'+type7[1]+'.html',
    unit_link='/informationobject/'+unit[1]+'.html',
    member_link='/object/'+member[1]+'.html',
    member1_link='/object/'+member1[1]+'.html',
    member2_link='/object/'+member2[1]+'.html',
    member3_link='/object/'+member3[1]+'.html',
    member4_link='/object/'+member4[1]+'.html',
    relatedAgent_link='/object/'+relatedAgent[1]+'.html',
    space_link='/object/'+space[1]+'.html',
    space1_link='/object/'+space1[1]+'.html',
    space2_link='/object/'+space2[1]+'.html',
    space3_link='/object/'+space3[1]+'.html',
    space4_link='/object/'+space4[1]+'.html',
    space5_link='/object/'+space5[1]+'.html',
    objectRole_link='/objectrole/'+objectRole[1]+'.html',
    objectRole1_link='/objectrole/'+objectRole1[1]+'.html',
    objectRole2_link='/objectrole/'+objectRole2[1]+'.html',
    objectRole3_link='/objectrole/'+objectRole3[1]+'.html',
    objectRole4_link='/objectrole/'+objectRole4[1]+'.html',
    objectRole5_link='/objectrole/'+objectRole5[1]+'.html',
    objectRole6_link='/objectrole/'+objectRole6[1]+'.html',
    objectRole7_link='/objectrole/'+objectRole7[1]+'.html',
    objectRole8_link='/objectrole/'+objectRole8[1]+'.html',
    objectRole9_link='/objectrole/'+objectRole9[1]+'.html',
    objectRole10_link='/objectrole/'+objectRole10[1]+'.html',
    objectRole11_link='/objectrole/'+objectRole11[1]+'.html',
    objectRole12_link='/objectrole/'+objectRole12[1]+'.html',
    objectRole13_link='/objectrole/'+objectRole13[1]+'.html',
    objectRole14_link='/objectrole/'+objectRole14[1]+'.html',
    objectRole15_link='/objectrole/'+objectRole15[1]+'.html',
    objectRole16_link='/objectrole/'+objectRole16[1]+'.html',
    objectRole17_link='/objectrole/'+objectRole17[1]+'.html',
    objectRole18_link='/objectrole/'+objectRole18[1]+'.html',
    objectRole19_link='/objectrole/'+objectRole19[1]+'.html',
    sameEntity_link='/object/'+sameEntity[1]+'.html',
    sameEntity1_link='/object/'+sameEntity1[1]+'.html',
   )
   
@app.route("/term/<IRI>.html")    
def term(IRI):
    term = term_data[IRI]
    type1=term_data[term[3]]
    if term[4]==term[4]:
      domain=term_data[term[4]]
    else:
      domain=term_data['FAILSAFE']
    if term[5]==term[5]:
      range0=term_data[term[5]]
    else:
      range0=term_data['FAILSAFE']
    if term[6]==term[6]:
      inverse=term_data[term[6]]
    else:
      inverse=term_data['FAILSAFE']
    if term[7]==term[7]:
      property0=term_data[term[7]]
    else:
      property0=term_data['FAILSAFE']
    if term[8]==term[8]:
      class0=term_data[term[8]]
    else:
      class0=term_data['FAILSAFE']
    if term[9]==term[9]:
      class1=term_data[term[9]]
    else:
      class1=term_data['FAILSAFE']
    if term[10]==term[10]:
      class2=term_data[term[10]]
    else:
      class2=term_data['FAILSAFE']
    if term[11]==term[11]:
      class3=term_data[term[11]]
    else:
      class3=term_data['FAILSAFE']
    return render_template("ontology.html",
    label=term[2],

    type1L=type1[2],
    domainL=domain[2],
    range0L=range0[2],
    inverseL=inverse[2],
    property0L=property0[2],
    class0L=class0[2],
    class1L=class1[2],
    class2L=class2[2],
    class3L=class3[2],
    comment=term[12],
    
    type1_link='/term/'+type1[1]+'.html',
    domain_link='/term/'+domain[1]+'.html',
    range0_link='/term/'+range0[1]+'.html',
    inverse_link='/term/'+inverse[1]+'.html',
    property0_link='/term/'+property0[1]+'.html',
    class0_link='/term/'+class0[1]+'.html',
    class1_link='/term/'+class1[1]+'.html',
    class2_link='/term/'+class2[1]+'.html',
    class3_link='/term/'+class3[1]+'.html',
   )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)