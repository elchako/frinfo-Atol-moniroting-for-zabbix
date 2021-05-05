# -*- coding: utf-8 -*-
from libfptr10 import IFptr
#import libfptr10
import os
import codecs
fptr = IFptr(r"C:\FR\fptr10.dll")
#fptr = IFptr("")
version = fptr.version()
with open('FR_info', 'w', encoding='utf-8') as f:
    f.write("Версия ДТО: " +'#' +str(version) + '#' + '\t')


fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_USB))
##fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
##fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM1")
##fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))

res=fptr.applySingleSettings()
##print (res);

fptr.open()

isOpened = fptr.isOpened()
#print ("Opened:"+str(isOpened));

if isOpened==0:
##    print ("9) Доступность:",0)
##    exit(1)
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM1")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    res=fptr.applySingleSettings()
    fptr.open()

    isOpened = fptr.isOpened()

if isOpened==0:
##    print ("9) Доступность:",0)
##    exit(1)
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM2")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    res=fptr.applySingleSettings()
    fptr.open()

    isOpened = fptr.isOpened()
if isOpened==0:
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM3")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    res=fptr.applySingleSettings()
    fptr.open()

    isOpened = fptr.isOpened()
if isOpened==0:
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM4")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    res=fptr.applySingleSettings()
    fptr.open()

    isOpened = fptr.isOpened()
if isOpened==0:
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM5")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    res=fptr.applySingleSettings()
    fptr.open()

    isOpened = fptr.isOpened()
if isOpened==0:
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM6")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    res=fptr.applySingleSettings()
    fptr.open()

    isOpened = fptr.isOpened()
##    exit(1)

fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_STATUS)
fptr.queryData()
serialNumber    = fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)
modelName       = fptr.getParamString(IFptr.LIBFPTR_PARAM_MODEL_NAME)
firmwareVersion = fptr.getParamString(IFptr.LIBFPTR_PARAM_UNIT_VERSION)
smena = fptr.getParamString(IFptr.LIBFPTR_PARAM_SHIFT_STATE)
numberCheck = fptr.getParamString(IFptr.LIBFPTR_PARAM_DOCUMENT_NUMBER)
dateTime = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)

with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("00) Время ФР: " + '#' + str(dateTime) + '#' + '\t')
    f.write ("01) Модель ФР: " + '#' + str(modelName) + '#' + '\t')
    f.write("02) Номер ФР: " + '#' + str(serialNumber) + '#' + '\t')
    f.write("03) Прошивка: " + '#' + str(firmwareVersion) + '#' + '\t')
    if smena == "0":
        f.write("04) Смена: #Закрыта#" + '\t')
    if smena == "1":
        f.write("04) Смена: #Открыта#" + '#' + '\t')
        f.write("05) Номер чека: " + '#' + str(numberCheck) + '#' + '\t')

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_REG_INFO)
fptr.fnQueryData()
organizationName            = fptr.getParamString(1048)
ffdVersion                  = fptr.getParamInt(1209)
ofdVATIN                    = fptr.getParamString(1017)
adress_mag                  = fptr.getParamString(1009)
ofdName                     = fptr.getParamString(1046)
regNumberFN                 = fptr.getParamString(1037)

with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("06) Организация: " + '#' + str(organizationName) + '#' + '\t')
    f.write("07) Адрес магазина: " + '#' + str(adress_mag) + '#' + '\t')
    f.write("08) ОФД: "+ '#' +str(ofdName) + '#' + '\t')
    f.write("08_1) ИНН ОФД" + '#' + str(ofdVATIN) + '#' + '\t')
    f.write("09) Версия ФФД: " + '#' + str(ffdVersion) + '#' + '\t')
    f.write("10) Регномер ФН: " + '#' + str(regNumberFN) + '#' + '\t')

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
fptr.fnQueryData()

fnSerial            = fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)
fnExhausted         = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_RESOURCE_EXHAUSTED)
fnMemoryOverflow    = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_MEMORY_OVERFLOW)
fnOfdTimeout        = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_OFD_TIMEOUT)
fnCriticalError     = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_CRITICAL_ERROR)
with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("11) Номер ФН: " + '#' + str(fnSerial) + '#' + '\t')
    f.write("12) Пямять ФН переполнена:" + '#' + str(fnMemoryOverflow) + '#' + '\t')
    f.write("13) Исчерпан ресурс ФН: " + '#' + str(fnExhausted) + '#' + '\t')
    f.write("14) Критическая ошибка ФН: " + '#' + str(fnCriticalError) + '#' + '\t')

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_OFD_EXCHANGE_STATUS)
fptr.fnQueryData()

exchangeStatus      = fptr.getParamInt(IFptr.LIBFPTR_PARAM_OFD_EXCHANGE_STATUS)
unsentCount         = fptr.getParamInt(IFptr.LIBFPTR_PARAM_DOCUMENTS_COUNT)
firstUnsentNumber   = fptr.getParamInt(IFptr.LIBFPTR_PARAM_DOCUMENT_NUMBER)
ofdMessageRead      = fptr.getParamBool(IFptr.LIBFPTR_PARAM_OFD_MESSAGE_READ)
dateTime            = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)
with open('FR_info', 'a', encoding='utf-8') as f:
    if exchangeStatus == 0:
        f.write("15) Статус обмена с ОФД: #соединение установлено#" + '\t')
    if exchangeStatus == 1:
        f.write("15) Статус обмена с ОФД: #есть сообщение для передачи в ОФД#" + '\t')
    if exchangeStatus == 2:
        f.write("15) Статус обмена с ОФД: #ожидание ответного сообщения от ОФД#" + '\t')
    if exchangeStatus == 3:
        f.write("15) Статус обмена с ОФД: #есть команда от ОФД#" + '\t')
    if exchangeStatus == 4:
        f.write("15) Статус обмена с ОФД: #изменились настройки соединения с ОФД#" + '\t')
    if exchangeStatus == 5:
        f.write("15) Статус обмена с ОФД: #ожидание ответа на команду от ОФД#" + '\t')
    f.write("16) Количество неотправленных чеков: " + '#' + str(unsentCount) + '#' + '\t')
    f.write("17) Номер первого неотправленного документа: " + '#' + str(firstUnsentNumber) + '#' + '\t')
    f.write("18) Флаг наличия сообщения для ОФД: " + '#' + str(ofdMessageRead) + '#' + '\t')
    f.write("19) Первый неотправленный документ: " + '#' + str(dateTime) + '#' + '\t')

fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_LAST_SENT_OFD_DOCUMENT_DATE_TIME)
fptr.queryData()
dateTime = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)
with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("20) Последний успешный обмен с ОФД: " + '#' + str(dateTime) + '#' + '\t')

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY)
fptr.fnQueryData()
dateTime            = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)
with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("21) Дата окончания ФН: " + '#' + str(dateTime) + '#' + '\t')

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_ERRORS)
fptr.fnQueryData()
networkErrorText    = fptr.getParamString(IFptr.LIBFPTR_PARAM_NETWORK_ERROR_TEXT)
ofdErrorText        = fptr.getParamString(IFptr.LIBFPTR_PARAM_OFD_ERROR_TEXT)
fnErrorText         = fptr.getParamString(IFptr.LIBFPTR_PARAM_FN_ERROR_TEXT)
with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("22) Ошибка сети: " + '#' + str(networkErrorText) + '#' + '\t')
    f.write("23) Ошибка ОФД: " + '#' + str(ofdErrorText) + '#' + '\t')
    f.write("24) Ошибка ФН: " + '#' + str(fnErrorText) + '#' + '\t')

#установка адреса ОФД
##fptr.setParam(IFptr.LIBFPTR_PARAM_SETTING_ID, 273)
##fptr.setParam(IFptr.LIBFPTR_PARAM_SETTING_VALUE, "gate.ofd.ru")
##fptr.writeDeviceSetting()
#считать даные ОФД
fptr.setParam(IFptr.LIBFPTR_PARAM_SETTING_ID, 273)
fptr.readDeviceSetting()
settingValue = fptr.getParamString(IFptr.LIBFPTR_PARAM_SETTING_VALUE)
with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("25) Адрес ОФД: " + '#' + str(settingValue) + '#' + '\t')
fptr.setParam(IFptr.LIBFPTR_PARAM_SETTING_ID, 274)
fptr.readDeviceSetting()
settingValue = fptr.getParamString(IFptr.LIBFPTR_PARAM_SETTING_VALUE)
with open('FR_info', 'a', encoding='utf-8') as f:
    f.write("26) Порт ОФД: " + '#' + str(settingValue) + '#' + '\t')
fptr.setParam(IFptr.LIBFPTR_PARAM_SETTING_ID, 276)
fptr.readDeviceSetting()
settingValue = fptr.getParamString(IFptr.LIBFPTR_PARAM_SETTING_VALUE)
with open('FR_info', 'a', encoding='utf-8') as f:
    if settingValue == "1":
       f.write("27) Канал обмена: #EoU#" + '\t')
    if settingValue == "2":
       f.write("27) Канал обмена: #Ethernet#" + '\t')
    if settingValue == "5":
       f.write("27) Канал обмена: #EoT#" + '\t')

fptr.setParam(IFptr.LIBFPTR_PARAM_SETTING_ID, 239)
fptr.readDeviceSetting()
settingValue = fptr.getParamString(IFptr.LIBFPTR_PARAM_SETTING_VALUE)
with open('FR_info', 'a', encoding='utf-8') as f:
    if settingValue == "0":
       f.write("28) Подключение: #COM#" + '\t')
    if settingValue == "4":
       f.write("28) Подключение: #USB#" + '\t')



f.close()
fptr.close()
del fptr
