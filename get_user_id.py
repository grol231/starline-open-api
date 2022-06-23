#!/usr/bin/python3
import logging
import requests
import argparse


__author__ = "Kosterev Grigoriy <kosterev@starline.ru>"
__date__ = "13.10.2018"


def get_user_id(slid_token):
    """
    Возвращает user_id. Не злоупотребляйте методом /auth.slid, так как сервер может потребовать каптчу при частых
    обращениях. Желательно user_id кэшировать.
    :param slid_token: Токен StarLineID
    :return: Токен пользователя на StarLineAPI
    """
    url = 'https://developer.starline.ru/json/v2/auth.slid'
    logging.info('execute request: {}'.format(url))
    data = {
        'slid_token': slid_token
    }
    r = requests.post(url, json=data)
    response = r.json()
    logging.info('response info: {}'.format(r))
    logging.info('response data: {}'.format(response))
    user_id = response["user_id"]
    logging.info('user_id: {}'.format(user_id))
    return user_id


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--slid_token", dest="slidToken", help="StarLineID Token", default="", required=True)
    args = parser.parse_args()
    logging.info("slidToken: {}".format(args.slidToken))
    return args


def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    args = get_args()
    get_user_id(args.slidToken)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(e)