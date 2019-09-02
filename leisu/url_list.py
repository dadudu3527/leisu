"""
一共585个赛事链接，页面结构相同

"""

ball_url_list = ['../zuqiu-9021', '../zuqiu-9048', '../zuqiu-9042',
                 '../zuqiu-9041', '../zuqiu-9102', '../zuqiu-9094',
                 '../zuqiu-9093', '../zuqiu-9159', '../zuqiu-9154',
                 '../zuqiu-9161', '../zuqiu-8718', '../zuqiu-9230',
                 '../zuqiu-9231', '../zuqiu-9229', '../zuqiu-491',
                 '../zuqiu-495', '../zuqiu-9055', '../zuqiu-9189',
                 '../zuqiu-9187', '../zuqiu-8749', '../zuqiu-8776',
                 '../zuqiu-9029', '../zuqiu-564', '../zuqiu-8759',
                 '../zuqiu-574', '../zuqiu-9263', '../zuqiu-9200',
                 '../zuqiu-9206', '../zuqiu-9257', '../zuqiu-9121',
                 '../zuqiu-9168', '../zuqiu-9205', '../zuqiu-9245',
                 '../zuqiu-617', '../zuqiu-8700', '../zuqiu-8719',
                 '../zuqiu-9170', '../zuqiu-5223', '../zuqiu-8925',
                 '../zuqiu-8835', '../zuqiu-9178', '../zuqiu-8723',
                 '../zuqiu-9092', '../zuqiu-9101', '../zuqiu-9125',
                 '../zuqiu-8699', '../zuqiu-8687', '../zuqiu-8672',
                 '../zuqiu-8507', '../zuqiu-9219', '../zuqiu-8768',
                 '../zuqiu-9067', '../zuqiu-9073', '../zuqiu-9095',
                 '../zuqiu-9061', '../zuqiu-9174', '../zuqiu-9162',
                 '../zuqiu-9212', '../zuqiu-9030', '../zuqiu-9266',
                 '../zuqiu-9183', '../zuqiu-9032', '../zuqiu-869',
                 '../zuqiu-5671', '../zuqiu-9026', '../zuqiu-9033',
                 '../zuqiu-9120', '../zuqiu-9135', '../zuqiu-9246',
                 '../zuqiu-9213', '../zuqiu-8736', '../zuqiu-9148',
                 '../zuqiu-9185', '../zuqiu-9104', '../zuqiu-9151',
                 '../zuqiu-9204', '../zuqiu-9232', '../zuqiu-8670',
                 '../zuqiu-9140', '../zuqiu-9191', '../zuqiu-9046',
                 '../zuqiu-9052', '../zuqiu-9053', '../zuqiu-9054',
                 '../zuqiu-9166', '../zuqiu-8646', '../zuqiu-8871',
                 '../zuqiu-9207', '../zuqiu-9113', '../zuqiu-9196',
                 '../zuqiu-9027', '../zuqiu-9035', '../zuqiu-1173',
                 '../zuqiu-1176', '../zuqiu-9220', '../zuqiu-9038',
                 '../zuqiu-9258', '../zuqiu-9077', '../zuqiu-9105',
                 '../zuqiu-5748', '../zuqiu-9262', '../zuqiu-9251',
                 '../zuqiu-9259', '../zuqiu-5761', '../zuqiu-9149',
                 '../zuqiu-9078', '../zuqiu-9241', '../zuqiu-8790',
                 '../zuqiu-8849', '../zuqiu-8963', '../zuqiu-8966',
                 '../zuqiu-8873', '../zuqiu-8944', '../zuqiu-8962',
                 '../zuqiu-8298', '../zuqiu-9015', '../zuqiu-1354',
                 '../zuqiu-8715', '../zuqiu-8950', '../zuqiu-8956',
                 '../zuqiu-8985', '../zuqiu-8938', '../zuqiu-8834',
                 '../zuqiu-1426', '../zuqiu-8789', '../zuqiu-8822',
                 '../zuqiu-8976', '../zuqiu-8940', '../zuqiu-8943',
                 '../zuqiu-8986', '../zuqiu-1497', '../zuqiu-8920',
                 '../zuqiu-9020', '../zuqiu-9085', '../zuqiu-9083',
                 '../zuqiu-9240', '../zuqiu-9180', '../zuqiu-9208',
                 '../zuqiu-9108', '../zuqiu-1560', '../zuqiu-9192',
                 '../zuqiu-8717', '../zuqiu-9222', '../zuqiu-9056',
                 '../zuqiu-9057', '../zuqiu-9109', '../zuqiu-9234',
                 '../zuqiu-9119', '../zuqiu-9045', '../zuqiu-9063',
                 '../zuqiu-9072', '../zuqiu-9224', '../zuqiu-8798',
                 '../zuqiu-8814', '../zuqiu-8913', '../zuqiu-9181',
                 '../zuqiu-1726', '../zuqiu-9103', '../zuqiu-9112',
                 '../zuqiu-9203', '../zuqiu-1756', '../zuqiu-8751',
                 '../zuqiu-9022', '../zuqiu-9024', '../zuqiu-9117',
                 '../zuqiu-9110', '../zuqiu-8980', '../zuqiu-9124',
                 '../zuqiu-9096', '../zuqiu-8868', '../zuqiu-9018',
                 '../zuqiu-9043', '../zuqiu-9050', '../zuqiu-9115',
                 '../zuqiu-9202', '../zuqiu-9193', '../zuqiu-1875',
                 '../zuqiu-9039', '../zuqiu-9051', '../zuqiu-9100',
                 '../zuqiu-9165', '../zuqiu-9238', '../zuqiu-9167',
                 '../zuqiu-8404', '../zuqiu-9065', '../zuqiu-9075',
                 '../zuqiu-9106', '../zuqiu-8523', '../zuqiu-9173',
                 '../zuqiu-9107', '../zuqiu-9150', '../zuqiu-1994',
                 '../zuqiu-9089', '../zuqiu-8746', '../zuqiu-9248',
                 '../zuqiu-9071', '../zuqiu-9190', '../zuqiu-9176',
                 '../zuqiu-9097', '../zuqiu-5277', '../zuqiu-9040',
                 '../zuqiu-9036', '../zuqiu-9136', '../zuqiu-8369',
                 '../zuqiu-8829', '../zuqiu-8830', '../zuqiu-8994',
                 '../zuqiu-8992', '../zuqiu-8997', '../zuqiu-8887',
                 '../zuqiu-8869', '../zuqiu-8866', '../zuqiu-8864',
                 '../zuqiu-8824', '../zuqiu-8981', '../zuqiu-8804',
                 '../zuqiu-8811', '../zuqiu-8825', '../zuqiu-8812',
                 '../zuqiu-8895', '../zuqiu-8959', '../zuqiu-8916',
                 '../zuqiu-9004', '../zuqiu-8403', '../zuqiu-8915',
                 '../zuqiu-8973', '../zuqiu-8971', '../zuqiu-9019',
                 '../zuqiu-8901', '../zuqiu-8949', '../zuqiu-8987',
                 '../zuqiu-9066', '../zuqiu-8600', '../zuqiu-8611',
                 '../zuqiu-8739', '../zuqiu-9179', '../zuqiu-9079',
                 '../zuqiu-9099', '../zuqiu-9226', '../zuqiu-2342',
                 '../zuqiu-8720', '../zuqiu-2362', '../zuqiu-2370',
                 '../zuqiu-9218', '../zuqiu-9137', '../zuqiu-9160',
                 '../zuqiu-9272', '../zuqiu-9273', '../zuqiu-2414',
                 '../zuqiu-2417', '../zuqiu-8616', '../zuqiu-8763',
                 '../zuqiu-2429', '../zuqiu-9260', '../zuqiu-2443',
                 '../zuqiu-2444', '../zuqiu-9197', '../zuqiu-2452',
                 '../zuqiu-9047', '../zuqiu-9215', '../zuqiu-9184',
                 '../zuqiu-9058', '../zuqiu-9060', '../zuqiu-8722',
                 '../zuqiu-9080', '../zuqiu-9074', '../zuqiu-9158',
                 '../zuqiu-9211', '../zuqiu-2553', '../zuqiu-9138',
                 '../zuqiu-8701', '../zuqiu-8769', '../zuqiu-8725',
                 '../zuqiu-9062', '../zuqiu-9034', '../zuqiu-8542',
                 '../zuqiu-9028', '../zuqiu-9243', '../zuqiu-8702',
                 '../zuqiu-8752', '../zuqiu-9177', '../zuqiu-9128',
                 '../zuqiu-9134', '../zuqiu-9249', '../zuqiu-8695',
                 '../zuqiu-8919', '../zuqiu-8965', '../zuqiu-8934',
                 '../zuqiu-9059', '../zuqiu-8709', '../zuqiu-8859',
                 '../zuqiu-8910', '../zuqiu-8917', '../zuqiu-8955',
                 '../zuqiu-9086', '../zuqiu-8820', '../zuqiu-8933',
                 '../zuqiu-8964', '../zuqiu-8991', '../zuqiu-9139',
                 '../zuqiu-9201', '../zuqiu-8714', '../zuqiu-9081',
                 '../zuqiu-9261', '../zuqiu-9084', '../zuqiu-9253',
                 '../zuqiu-8735', '../zuqiu-8705', '../zuqiu-8783',
                 '../zuqiu-9267', '../zuqiu-2866', '../zuqiu-9132',
                 '../zuqiu-8747', '../zuqiu-8926', '../zuqiu-8972',
                 '../zuqiu-8902', '../zuqiu-8903', '../zuqiu-8975',
                 '../zuqiu-9216', '../zuqiu-8778', '../zuqiu-9171',
                 '../zuqiu-9250', '../zuqiu-9236', '../zuqiu-8708',
                 '../zuqiu-8839', '../zuqiu-8721', '../zuqiu-9217',
                 '../zuqiu-9127', '../zuqiu-9210', '../zuqiu-9144',
                 '../zuqiu-8823', '../zuqiu-8977', '../zuqiu-8810',
                 '../zuqiu-9145', '../zuqiu-8666', '../zuqiu-8905',
                 '../zuqiu-8953', '../zuqiu-8787', '../zuqiu-8815',
                 '../zuqiu-8802', '../zuqiu-8805', '../zuqiu-8806',
                 '../zuqiu-8807', '../zuqiu-8808', '../zuqiu-8836',
                 '../zuqiu-8809', '../zuqiu-8838', '../zuqiu-8819',
                 '../zuqiu-8821', '../zuqiu-8841', '../zuqiu-8865',
                 '../zuqiu-8800', '../zuqiu-9049', '../zuqiu-8832',
                 '../zuqiu-9031', '../zuqiu-5687', '../zuqiu-8927',
                 '../zuqiu-9141', '../zuqiu-8773', '../zuqiu-8984',
                 '../zuqiu-9009', '../zuqiu-8828', '../zuqiu-8921',
                 '../zuqiu-8974', '../zuqiu-6770', '../zuqiu-8993',
                 '../zuqiu-6683', '../zuqiu-8876', '../zuqiu-8877',
                 '../zuqiu-8937', '../zuqiu-8947', '../zuqiu-9064',
                 '../zuqiu-9082', '../zuqiu-9152', '../zuqiu-9118',
                 '../zuqiu-8498', '../zuqiu-8793', '../zuqiu-8988',
                 '../zuqiu-8884', '../zuqiu-5350', '../zuqiu-8880',
                 '../zuqiu-3419', '../zuqiu-8840', '../zuqiu-8861',
                 '../zuqiu-8879', '../zuqiu-8870', '../zuqiu-8842',
                 '../zuqiu-9164', '../zuqiu-8831', '../zuqiu-5175',
                 '../zuqiu-9146', '../zuqiu-8998', '../zuqiu-9013',
                 '../zuqiu-9111', '../zuqiu-3521', '../zuqiu-9133',
                 '../zuqiu-9155', '../zuqiu-8431', '../zuqiu-8872',
                 '../zuqiu-8914', '../zuqiu-8929', '../zuqiu-9268',
                 '../zuqiu-8983', '../zuqiu-8689', '../zuqiu-8844',
                 '../zuqiu-3802', '../zuqiu-3803', '../zuqiu-3804',
                 '../zuqiu-3805', '../zuqiu-3806', '../zuqiu-8892',
                 '../zuqiu-8908', '../zuqiu-7422', '../zuqiu-7423',
                 '../zuqiu-8748', '../zuqiu-3830', '../zuqiu-3837',
                 '../zuqiu-8797', '../zuqiu-3847', '../zuqiu-9163',
                 '../zuqiu-8813', '../zuqiu-8078', '../zuqiu-3870',
                 '../zuqiu-7442', '../zuqiu-8691', '../zuqiu-5695',
                 '../zuqiu-7427', '../zuqiu-8801', '../zuqiu-8851',
                 '../zuqiu-8853', '../zuqiu-8931', '../zuqiu-8941',
                 '../zuqiu-8948', '../zuqiu-8878', '../zuqiu-3920',
                 '../zuqiu-3924', '../zuqiu-8907', '../zuqiu-8883',
                 '../zuqiu-9003', '../zuqiu-8740', '../zuqiu-8942',
                 '../zuqiu-7361', '../zuqiu-8765', '../zuqiu-5698',
                 '../zuqiu-8967', '../zuqiu-8850', '../zuqiu-8893',
                 '../zuqiu-8891', '../zuqiu-8951', '../zuqiu-8978',
                 '../zuqiu-9002', '../zuqiu-8922', '../zuqiu-5005',
                 '../zuqiu-9265', '../zuqiu-8912', '../zuqiu-8874',
                 '../zuqiu-8882', '../zuqiu-8894', '../zuqiu-8888',
                 '../zuqiu-8923', '../zuqiu-8968', '../zuqiu-8860',
                 '../zuqiu-8755', '../zuqiu-8898', '../zuqiu-8897',
                 '../zuqiu-8744', '../zuqiu-8881', '../zuqiu-4139',
                 '../zuqiu-4140', '../zuqiu-4141', '../zuqiu-8845',
                 '../zuqiu-9037', '../zuqiu-4153', '../zuqiu-9129',
                 '../zuqiu-9098', '../zuqiu-8911', '../zuqiu-8899',
                 '../zuqiu-8875', '../zuqiu-8946', '../zuqiu-8909',
                 '../zuqiu-8712', '../zuqiu-7698', '../zuqiu-9252',
                 '../zuqiu-9237', '../zuqiu-8742', '../zuqiu-8758',
                 '../zuqiu-7481', '../zuqiu-4208', '../zuqiu-8795',
                 '../zuqiu-7457', '../zuqiu-7514', '../zuqiu-9244',
                 '../zuqiu-9228', '../zuqiu-8680', '../zuqiu-8527',
                 '../zuqiu-9131', '../zuqiu-8761', '../zuqiu-8732',
                 '../zuqiu-9256', '../zuqiu-4294', '../zuqiu-8852',
                 '../zuqiu-8546', '../zuqiu-7208', '../zuqiu-8854',
                 '../zuqiu-8855', '../zuqiu-8961', '../zuqiu-9182',
                 '../zuqiu-4362', '../zuqiu-4363', '../zuqiu-9195',
                 '../zuqiu-8706', '../zuqiu-8729', '../zuqiu-8682',
                 '../zuqiu-8784', '../zuqiu-4392', '../zuqiu-8995',
                 '../zuqiu-9242', '../zuqiu-8837', '../zuqiu-6802',
                 '../zuqiu-8339', '../zuqiu-9223', '../zuqiu-4430',
                 '../zuqiu-4433', '../zuqiu-4438', '../zuqiu-8655',
                 '../zuqiu-8924', '../zuqiu-7334', '../zuqiu-8856',
                 '../zuqiu-8867', '../zuqiu-8957', '../zuqiu-8896',
                 '../zuqiu-8396', '../zuqiu-8659', '../zuqiu-8684',
                 '../zuqiu-8954', '../zuqiu-8779', '../zuqiu-8786',
                 '../zuqiu-4533', '../zuqiu-8624', '../zuqiu-8710',
                 '../zuqiu-9255', '../zuqiu-8696', '../zuqiu-8858',
                 '../zuqiu-9130', '../zuqiu-8697', '../zuqiu-8745',
                 '../zuqiu-8726', '../zuqiu-6972', '../zuqiu-8487',
                 '../zuqiu-8932', '../zuqiu-8889', '../zuqiu-8970',
                 '../zuqiu-8952', '../zuqiu-8833', '../zuqiu-9044',
                 '../zuqiu-4632', '../zuqiu-8996', '../zuqiu-9000',
                 '../zuqiu-8777', '../zuqiu-8918', '../zuqiu-8960',
                 '../zuqiu-8989', '../zuqiu-9006', '../zuqiu-8900',
                 '../zuqiu-8826', '../zuqiu-8738', '../zuqiu-9114',
                 '../zuqiu-9233', '../zuqiu-8566', '../zuqiu-8743',
                 '../zuqiu-8827', '../zuqiu-8550', '../zuqiu-8660',
                 '../zuqiu-9269', '../zuqiu-9247', '../zuqiu-8716',
                 '../zuqiu-8737', '../zuqiu-9209', '../zuqiu-9254',
                 '../zuqiu-8766', '../zuqiu-8570', '../zuqiu-8733',
                 '../zuqiu-9225', '../zuqiu-8019', '../zuqiu-8767']

# print(len(ball_url_list))