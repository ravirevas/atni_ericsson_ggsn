import binascii
from atni.parsers.utilities import parseTimestamp, append_timezone_offset


def parseMcc(data):
    mcc = ""
    if len(data) == 6:
        mcc = data[1:2] + data[0:1] + data[3:4]
        mcc = mcc.replace("f", "")

    return mcc


def parseMnc(data):
    mnc = ""
    if len(data) == 6:
        mnc = data[5:6] + data[4:5] + data[2:3]
        mnc = mnc.replace("f", "")

    return mnc


class ProcessZTEumtsMOSMSRecord:

    def __init__(self):
        pass

    @staticmethod
    def process_mosms_records(mosms_record, file_id, file_name):

        if mosms_record.getComponentByName("basicService") is None:
            basic_service = ""
        else:
            basic_service_choice = mosms_record.getComponentByName("basicService")
            basic_service_choice_hexvalue = basic_service_choice.getComponent().prettyPrint()
            if basic_service_choice_hexvalue == "0x11":
                basic_service = "teleservice"
            else:
                basic_service = "bearerservice"

        if mosms_record.getComponentByName("cAMELSMSInformation") is not None:
            camel_sms_information = mosms_record.getComponentByName("cAMELSMSInformation")
            camel_smsc_address = str(camel_sms_information.getComponentByName("cAMELSMSCAddress"))
            calling_party_number = str(camel_sms_information.getComponentByName("callingPartyNumber"))
            if camel_sms_information is None:
                default_sms_handling = ""
            else:
                default_sms_handling_tmp = long(str(camel_sms_information.getComponentByName("defaultSMSHandling")))
                default_sms_handling = ""
                if default_sms_handling_tmp == 0:
                    default_sms_handling = "continueTransaction"
                elif default_sms_handling_tmp == 1:
                    default_sms_handling = "releaseTransaction"
            destination_subscriber_number = binascii.hexlify(
                str(camel_sms_information.getComponentByName("destinationSubscriberNumber")))
            free_format_data = str(camel_sms_information.getComponentByName("freeFormatData"))
            gsm_scfaddress = str(camel_sms_information.getComponentByName("gsm-SCFAddress"))
            sms_reference_number = long(str(camel_sms_information.getComponentByName("smsRefrenceNumber")))
            service_key = long(str(camel_sms_information.getComponentByName("serviceKey")))
        else:
            camel_smsc_address = ""
            calling_party_number = ""
            default_sms_handling = ""
            destination_subscriber_number = ""
            free_format_data = ""
            gsm_scfaddress = ""
            sms_reference_number = -255
            service_key = -255

        if mosms_record.getComponentByName("callReference") is None:
            call_reference = ""
        else:
            call_reference = binascii.hexlify(str(mosms_record.getComponentByName("callReference")))

        if mosms_record.getComponentByName("concatenatedRecordNum") is None:
            concatenated_record_num = -255
        else:
            concatenated_record_num = long(str(mosms_record.getComponentByName("concatenatedRecordNum")))

        if mosms_record.getComponentByName("concatenatedRef") is None:
            concatenated_ref = -255
        else:
            concatenated_ref = long(str(mosms_record.getComponentByName("concatenatedRef")))

        if mosms_record.getComponentByName("destinationNumber") is None:
            destination_number = ""
        else:
            destination_number_binascii = binascii.hexlify(str(mosms_record.getComponentByName("destinationNumber")))
            destination_number_list = []
            destination_number_data = list(destination_number_binascii)
            for j in xrange(0, len(destination_number_data) - 1, 2):
                destination_number_list.append(destination_number_data[j+1] + "" + destination_number_data[j])
            destination_number_concatenated = ''.join(destination_number_list)
            destination_number = destination_number_concatenated[2:].replace("f", "")

        if mosms_record.getComponentByName("directSmsFlag") is None:
            direct_sms_flag = -255
        else:
            direct_sms_flag = long(str(mosms_record.getComponentByName("directSmsFlag")))

        if mosms_record.getComponentByName("exchangeIdentity") is None:
            exchange_identity = ""
        else:
            exchange_identity = str(mosms_record.getComponentByName("exchangeIdentity"))

        if mosms_record.getComponentByName("hotBillingTag") is None:
            hot_billing_tag = -255
        else:
            hot_billing_tag = long(str(mosms_record.getComponentByName("hotBillingTag")))

        if mosms_record.getComponentByName("hotBillingTag2") is None:
            hot_billing_tag2 = -255
        else:
            hot_billing_tag2 = long(str(mosms_record.getComponentByName("hotBillingTag2")))

        location = mosms_record.getComponentByName("location")
        if location is not None:
            location_area = binascii.hexlify(str(location.getComponentByName("locationArea")))
            location_area_str = str(location_area)
            location_cellid_binascii = location_area_str[10:14]
            format_location_cellid_binascii = int(location_cellid_binascii, 16)
            location_cellid = format(format_location_cellid_binascii, '05')
            location_area_code_binascii = location_area_str[6:10]
            format_location_area_code_binascii = int(location_area_code_binascii, 16)
            location_area_code = format(format_location_area_code_binascii, '05')
            location_plmn = parseMcc(location_area_str[0:6]) + parseMnc(location_area_str[0:6])
            location_sac = location_area_str[-4:]
        else:
            location_cellid = ''
            location_area_code = ''
            location_plmn = ''
            location_sac = ''

        if mosms_record.getComponentByName("locationExtension") is None:
            location_extension = ""
        else:
            location_extension_tmp = mosms_record.getComponentByName("locationExtension").prettyPrint()
            location_extension = location_extension_tmp[2:5]

        if mosms_record.getComponentByName("msClassmark") is None:
            ms_classmark = ""
        else:
            ms_classmark = binascii.hexlify(str(mosms_record.getComponentByName("msClassmark")))

        if mosms_record.getComponentByName("messageReference") is None:
            message_reference = ""
        else:
            message_reference = binascii.hexlify(str(mosms_record.getComponentByName("messageReference")))

        if mosms_record.getComponentByName("mscSPC14") is None:
            mscspc14 = ""
        else:
            mscspc14 = binascii.hexlify(str(mosms_record.getComponentByName("mscSPC14")))

        if mosms_record.getComponentByName("mscSPC24") is None:
            mscspc24 = ""
        else:
            mscspc24 = binascii.hexlify(str(mosms_record.getComponentByName("mscSPC24")))

        if mosms_record.getComponentByName("numOfConcatenated") is None:
            num_of_concatenated = -255
        else:
            num_of_concatenated = long(str(mosms_record.getComponentByName("numOfConcatenated")))

        if mosms_record.getComponentByName("operatorId") is None:
            operator_id = -255
        else:
            operator_id = long(str(mosms_record.getComponentByName("operatorId")))

        origination_time_tmp = binascii.hexlify(str(mosms_record.getComponentByName("originationTime")))
        origination_time = append_timezone_offset(parseTimestamp(origination_time_tmp))

        if mosms_record.getComponentByName("recordSequenceNumber") is None:
            record_sequence_number = ""
        else:
            record_sequence_number = binascii.hexlify(str(mosms_record.getComponentByName("recordSequenceNumber")))

        if mosms_record.getComponentByName("recordType") is None:
            record_type = -255
        else:
            record_type = long(str(mosms_record.getComponentByName("recordType")))

        if mosms_record.getComponentByName("recordingEntity") is None:
            recording_entity = ""
        else:
            recording_entity_binascii = binascii.hexlify(str(mosms_record.getComponentByName("recordingEntity")))
            recording_entity_list = []
            recording_entity_data = list(recording_entity_binascii)
            for l in xrange(0, len(recording_entity_data) - 1, 2):
                recording_entity_list.append(recording_entity_data[l+1] + "" + recording_entity_data[l])
            recording_entity_concatenated = ''.join(recording_entity_list)
            recording_entity_replace_f = recording_entity_concatenated.replace("f", "")
            recording_entity = recording_entity_replace_f[2:7] + recording_entity_replace_f[7:]

        if mosms_record.getComponentByName("sMSLength") is None:
            sms_length = ""
        else:
            sms_length = binascii.hexlify(str(mosms_record.getComponentByName("sMSLength")))

        if mosms_record.getComponentByName("servedIMEI") is None:
            served_imei = ""
        else:
            served_imei_binascii = binascii.hexlify(str(mosms_record.getComponentByName("servedIMEI")))
            served_imei_list = []
            served_imei_data = list(served_imei_binascii)
            for i in xrange(0, len(served_imei_data) - 1, 2):
                served_imei_list.append(served_imei_data[i + 1] + "" + served_imei_data[i])
            served_imei_concatenated = ''.join(served_imei_list)
            served_imei = served_imei_concatenated.replace("f", "")

        if mosms_record.getComponentByName("servedIMSI") is None:
            served_imsi = ""
        else:
            served_imsi_binascii = binascii.hexlify(str(mosms_record.getComponentByName("servedIMSI")))
            served_imsi_list = []
            served_imsi_data = list(served_imsi_binascii)
            for j in xrange(0, len(served_imsi_data) - 1, 2):
                served_imsi_list.append(served_imsi_data[j+1] + "" + served_imsi_data[j])
            served_imsi_concatenated = ''.join(served_imsi_list)
            served_imsi = served_imsi_concatenated.replace("f", "")

        if mosms_record.getComponentByName("servedMSISDN") is None:
            served_msisdn = ""
        else:
            served_msisdn_binascii = binascii.hexlify(str(mosms_record.getComponentByName("servedMSISDN")))
            served_msisdn_list = []
            served_msisdn_data = list(served_msisdn_binascii)
            for k in xrange(0, len(served_msisdn_data) - 1, 2):
                served_msisdn_list.append(served_msisdn_data[k+1] + "" + served_msisdn_data[k])
            served_msisdn_concatenated = ''.join(served_msisdn_list)
            served_msisdn_replace_f = served_msisdn_concatenated.replace("f", "")
            served_msisdn = served_msisdn_replace_f.replace(served_msisdn_replace_f[:3], '')

        if mosms_record.getComponentByName("serviceCentre") is None:
            service_centre = ""
        else:
            service_centre_binascii = binascii.hexlify(str(mosms_record.getComponentByName("serviceCentre")))
            service_centre_list = []
            service_centre_data = list(service_centre_binascii)
            for l in xrange(0, len(service_centre_data) - 1, 2):
                service_centre_list.append(service_centre_data[l+1] + "" + service_centre_data[l])
            service_centre_concatenated = ''.join(service_centre_list)
            service_centre_replace_f = service_centre_concatenated.replace("f", "")
            service_centre = service_centre_replace_f[2:7] + service_centre_replace_f[7:]

        if mosms_record.getComponentByName("smsResult") is None:
            sms_result = ""
        else:
            sms_result = mosms_record.getComponentByName("smsResult").getName()

        if mosms_record.getComponentByName("systemType") is None:
            system_type = ""
        else:
            system_type_tmp = long(str(mosms_record.getComponentByName("systemType")))
            system_type = ""
            if system_type_tmp == 0:
                system_type = "unknown"
            elif system_type_tmp == 1:
                system_type = "iuUTRAN"
            elif system_type_tmp == 2:
                system_type = "gERAN"

        if mosms_record.getComponentByName("tPMessageTypeIndicator") is None:
            tp_messagetype_indicator = ""
        else:
            tp_messagetype_indicator_tmp = long(str(mosms_record.getComponentByName("tPMessageTypeIndicator")))
            tp_messagetype_indicator = ""

            if tp_messagetype_indicator_tmp == 0:
                tp_messagetype_indicator = "sMS-DELIVER-REPORT"
            elif tp_messagetype_indicator_tmp == 1:
                tp_messagetype_indicator = "sMS-SUBMIT"
            elif tp_messagetype_indicator_tmp == 2:
                 tp_messagetype_indicator = "sMS-COMMAND"
            elif tp_messagetype_indicator_tmp == 3:
                 tp_messagetype_indicator = "reserved"

        if mosms_record.getComponentByName("transactionIdentification") is None:
            transaction_identification = ""
        else:
            transaction_identification = str(mosms_record.getComponentByName("transactionIdentification"))

        mosms_record = [basic_service, camel_smsc_address, calling_party_number, default_sms_handling,
                        destination_subscriber_number, free_format_data, gsm_scfaddress,
                        service_key, sms_reference_number,
                        call_reference, concatenated_record_num, concatenated_ref, destination_number,
                        direct_sms_flag, exchange_identity, file_id, hot_billing_tag, hot_billing_tag2,
                        location_cellid, location_extension, location_area_code, location_plmn, location_sac,
                        message_reference, ms_classmark, mscspc14, mscspc24, operator_id,
                        num_of_concatenated, origination_time, record_sequence_number, record_type, recording_entity,
                        sms_length, served_imei, served_imsi, served_msisdn, service_centre, sms_result,
                        system_type, tp_messagetype_indicator, transaction_identification,
                        long(origination_time.strftime("%Y%m%d")), long(origination_time.strftime("%H"))]

        return mosms_record
