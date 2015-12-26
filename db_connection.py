import cx_Oracle


def get_configuration():
    with open("config", encoding='utf-8') as config_file:
        parameters = {}
        for line in config_file:
            parameter, value = line.split(": ")
            parameter = parameter.rstrip()
            value = value.strip()
            parameters[parameter] = value

    info = "{}/{}@{}/{}".format(parameters["name"],
                                parameters["password"],
                                parameters["server and port"],
                                parameters["database service"])
    print("Server started with parameters:", info)
    return info

info = get_configuration()
con = cx_Oracle.connect(info)
cur = con.cursor()


def authorize_user(login, password):
    global con
    global cur

    authorize_result = {"success": False,
                        "role": 'user'}

    cur.execute('SELECT user_login_pk, user_password, user_role FROM users')
    for result in cur:
        if login == result[0] and password == result[1]:
            user_role = result[2]
            authorize_result["success"] = True
            authorize_result["role"] = user_role

    return authorize_result


def get_user_info(login, cost_date):
    global con
    global cur

    user_cost_number = "0"
    info_results = {"success": True,
                    "cost_category": '',
                    "cost_sum": '',
                    "cost_date": '',
                    "cost_comment": ''}

    cost_categorys = []
    cost_money_sums = []
    cost_dates = []
    cost_comments = []

    cur.execute('SELECT cost_number_fk FROM usercosts WHERE user_login_fk = \'{0}\''.format(login))
    for result_cost_number in cur:
        user_cost_number = result_cost_number[0]

    cur.execute('SELECT cost_category, cost_money_summ, cost_date, cost_comment'
                ' FROM costs WHERE cost_number = {0} AND cost_date LIKE \'{1}\''
                .format(user_cost_number, cost_date))

    print(cur)
    for result_user_info in cur:
        cost_categorys.append(result_user_info[0])
        cost_money_sums.append(result_user_info[1])
        cost_dates.append(str(result_user_info[2]))
        cost_comments.append(result_user_info[3])

    info_results['cost_category'] = cost_categorys
    info_results['cost_sum'] = cost_money_sums
    info_results['cost_date'] = cost_dates
    info_results['cost_comment'] = cost_comments

    return info_results


def add_new_cost(new_cost_data, login):
    global con
    global cur

    result = {
        "success": True
    }
    try:
        cur.execute('INSERT INTO costs(cost_number, cost_category, cost_money_summ, cost_date '
                    'VALUES (\'{0}\',\'{1}\', \'{2}\', \'{3}\'))'.format(new_cost_data['cost_number'],
                                                                         new_cost_data['cost_category'],
                                                                         new_cost_data['cost_money_summ'],
                                                                         new_cost_data['cost_date']))

        cur.execute('INSERT INTO usercosts(cost_number_fk, user_login_fk)'
                    ' VALUES (\'{0}\', \'{1}\')'.format(new_cost_data['cost_number'],
                                                        login))

        con.commit()
    except Exception as E:
        result['success'] = False
        con.rollback()

    return result


def get_plane(login, plane_month):
    global con
    global cur

    result = {
        "success": True
    }

    try:
        cur.execute('SELECT plane_money_summ FROM plane '
                    'WHERE user_login_fk = \'{0}\' AND plane_month = \'{1}\''. format(login, plane_month))
    except Exception as E:
        result['success'] = False

    return result

