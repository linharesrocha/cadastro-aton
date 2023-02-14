import pandas as pd
import pyodbc
import datetime
import pandas as pd
import warnings
import numpy as np
import os
import sys
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()



comando = f'''
SELECT CODID, COD_INTERNO, DESCRICAO, DESCRITIVO
FROM MATERIAIS
WHERE CODID IN('5', '6', '7', '8', '9', '10', '17', '23', '24', '26', '33', '76', '77', '101', '102', '103', '104', '105', '106', '111', '112', '114', '115', '116', '117', '119', '120', '121', '122', '123', '129', '130', '131', '132', '133', '134', '135', '143', '157', '163', '165', '167', '181', '184', '209', '210', '211', '212', '213', '252', '259', '260', '262', '269', '318', '325', '326', '327', '328', '334', '337', '339', '340', '341', '342', '348', '349', '350', '351', '352', '354', '355', '356', '358', '359', '360', '473', '474', '475', '478', '479', '480', '481', '482', '501', '564', '566', '570', '571', '572', '574', '579', '604', '628', '629', '630', '633', '634', '635', '638', '639', '640', '643', '644', '645', '649', '650', '651', '653', '654', '655', '657', '658', '659', '660', '661', '662', '663', '664', '666', '670', '671', '706', '715', 
'716', '721', '722', '726', '773', '983', '984', '986', '1009', '1011', '1013', '1027', '1039', '1040', '1044', '1068', '1069', '1080', '1081', '1082', '1083', '1108', '1111', '1113', '1114', '1115', '1132', '1133', '1134', '1136', '1137', '1138', '1211', '1266', '1278', '1279', '1283', '1284', '1293', '1294', '1347', '1348', '1387', '1431', '1432', '1433', '1434', '1435', '1495', '1496', '1499', '1500', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1525', '1550', '1551', '1552', '1553', '1554', '1555', '1556', '1557', '1558', '1559', '1560', '1561', '1562', '1563', '1564', '1565', '1566', '1567', '1653', '1654', '1655', '14', '16', '18', '19', '20', '21', '22', '27', '29', '31', '34', '35', '36', '37', '38', '41', '42', '44', '45', '46', '48', '49', '50', '51', '52', '55', '57', '58', '59', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '78', '80', '81', '83', '84', '86', '87', '88', '90', '92', '93', '94', '95', '96', '97', '155', '156', '185', '188', '189', '191', '192', '193', '198', '199', '200', '201', '203', '204', '205', '206', '207', '208', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', 
'227', '228', '229', '230', '231', '232', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '270', '272', '273', '275', '276', '277', '278', '279', '280', '282', '290', '291', '292', '293', '295', '296', '297', '330', '331', '333', '353', '362', '363', '364', '365', '366', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '380', '381', '382', '396', '397', '399', '407', '409', '410', '411', '412', '414', '415', '416', '417', '419', '420', '421', '422', '425', '426', '427', '428', '431', '432', '433', '434', '435', '436', '437', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '453', '454', '455', '456', '457', '458', '462', '465', '467', '468', '469', '470', '471', '477', '483', '484', '485', '492', '493', '498', '499', '502', '517', '518', '519', '520', '521', '522', '523', '546', '547', '585', '587', '589', '590', '594', '596', '597', '598', '599', '601', '605', '606', '607', '608', '609', '610', '611', '612', '613', '614', '615', '616', '618', '619', '620', '621', '622', '623', '624', '625', '626', '627', '672', '673', '674', '675', '676', '680', '681', '682', '683', '684', '685', '686', 
'687', '688', '691', '692', '693', '694', '696', '698', '704', '708', '710', '711', '727', '728', '730', '731', '732', '733', '734', '735', '736', '737', '738', '743', '748', '750', '751', '752', '753', '754', '755', '756', '757', '758', '759', '760', '771', '774', '775', '776', '777', '778', '779', '780', '781', '782', '787', '789', '790', '791', '796', '797', '798', '800', '801', '804', '805', '818', '819', '830', '845', '846', '849', '850', '851', '854', '855', '857', '858', '859', '860', '861', '1054', '1088', '1089', '1090', '1091', '1094', '1096', '1098', '1099', '1140', '1141', '1142', '1143', '1144', '1145', '1148', '1150', '1151', '1153', '1154', '1155', '1156', '1158', '1159', '1160', '1162', '1163', '1165', '1166', '1167', '1168', '1169', '1170', '1171', '1182', '1191', '1192', '1193', '1194', '1195', '1196', '1197', '1198', '1199', '1200', '1201', '1202', '1203', '1204', '1205', '1206', '1207', '1208', '1209', '1226', '1228', '1229', '1230', '1235', '1236', '1237', '1238', '1248', '1250', '1251', '1252', '1253', '1254', '1255', '1256', '1257', '1258', '1259', '1260', '1261', '1262', '1263', '1264', '1290', '1298', '1300', '1302', '1304', '1305', '1336', '1339', '1340', '1341', '1342', '1343', '1344', '1345', '1416', '1417', '1436', '1528', '1529', '1530', '1531', '1532', '1533', '1534', '1535', '1536', '1537', '1538', '1542', '1543', '1544', '1545', 
'1546', '1547', '1548', '1549', '1656', '1697')
'''

data = pd.read_sql(comando, conexao)

palavras = ['Hmmaston', 'Babyliss', 'Iphone', 'Apple', 'Smartband', 'Mi Band', 'Despertador', 'Pedido']


# função para procurar palavras na descrição
def procurar_palavras(descricao, palavras):
    # inicializar uma lista vazia para armazenar as palavras encontradas
    encontradas = []
    # percorrer cada palavra na lista de palavras a serem procuradas
    for palavra in palavras:
        # verificar se a palavra está presente na descrição
        if palavra in descricao:
            # se a palavra estiver presente, adicionar à lista de palavras encontradas
            encontradas.append(palavra)
    # se não foram encontradas palavras, retornar 'N/A'
    if len(encontradas) == 0:
        return 'N/A'
    # se foram encontradas palavras, retornar uma string contendo as palavras encontradas separadas por vírgulas
    else:
        return ', '.join(encontradas)

data['PALAVRAS_ENCONTRADAS'] = data['DESCRITIVO'].apply(lambda x: procurar_palavras(x, palavras))

data.to_excel('produtos_com_palavras_proibidas.xlsx', index=False)