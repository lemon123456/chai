import logging

from dsd.models import Province
from dsd.models.remote.province import Province as ProvinceRemote
from dsd.util import id_generator

logger = logging.getLogger(__name__)


def sync():
    all_remote_provinces = ProvinceRemote.objects.all()
    logger.info('all_remote_provinces=%s', len(all_remote_provinces))
    all_local_provinces = get_all_local_provinces(all_remote_provinces)
    logger.info('remote province length= %s' % len(all_local_provinces))
    all_valid_local_provinces = list(filter(is_valid_province, all_local_provinces))
    logger.info('all_valid_local_provinces length= %s' % len(list(all_valid_local_provinces)))
    save_provinces(all_valid_local_provinces)


def is_valid_province(province):
    if not province.province_name:
        return False
    return True


def get_all_local_provinces(all_remote_provinces):
    all_local_provinces = []
    for remote_province in all_remote_provinces:
        logger.info('remote province = %s' % remote_province.__dict__)
        remote_province.__dict__.pop('_state')
        local_province = Province(**remote_province.__dict__)
        local_province.uid = id_generator.generate_id()
        all_local_provinces.append(local_province)

    return all_local_provinces


def save_provinces(provinces):
    for province in provinces:
        logger.info('province = %s' % province.__dict__)
        filter_result = Province.objects.filter(province_name=province.province_name)
        if not filter_result.count():
            province.save()
            continue

        if is_updated(province):
            existing_province = Province.objects.get(province_name=province.province_name)
            province.id = existing_province.id
            province.uid = existing_province.uid
            province.save()


def is_updated(province_remote):
    province = Province.objects.get(province_name=province_remote.province_name)
    return province_remote.province_name != province.province_name or \
           province_remote.description != province.description or \
           province_remote.data_creation != province.data_creation or \
           province_remote.user_creation != province.user_creation or \
           province_remote.state != province.state
