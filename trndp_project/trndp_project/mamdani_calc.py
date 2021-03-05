import numpy as np
import skfuzzy as trndp
import matplotlib.pyplot as plt

def trndp_calc(data):
    gender = data['gender']
    # gender = "Male"
    id = str(data["id"])
    # id = "1"

    if gender == "Male":
        #Initialize Range
        cognitive = np.arange(0,37,1)
        cog_level = {}
        cog_level["low"] = trndp.trapmf(cognitive,[0,0,12,24])
        cog_level["med"] = trndp.trimf(cognitive,[20,26,33])
        cog_level["high"] = trndp.trapmf(cognitive,[32,34,36,36])
        # c_Low = trndp.trapmf(cognitive,[0,0,12,24])
        # c_Med = trndp.trimf(cognitive,[20,26,33])
        # c_High = trndp.trapmf(cognitive,[32,34,36,36])

        social = np.arange(0,53,1)
        soc_level = {}
        soc_level["low"] = trndp.trapmf(social,[0,0,16,32])
        soc_level["med"] = trndp.trimf(social,[29,36,44])
        soc_level["high"] = trndp.trapmf(social,[41,46,52,52])
        # s_Low = trndp.trapmf(social,[0,0,16,32])
        # s_Med = trndp.trimf(social,[29,36,44])
        # s_High = trndp.trapmf(social,[41,46,52,52])

        emotional = np.arange(0,65,1)
        emo_level = {}
        emo_level["low"] = trndp.trapmf(emotional,[0,0,18,37])
        emo_level["med"] = trndp.trimf(emotional,[30,39,44])
        emo_level["high"] = trndp.trapmf(emotional,[40,52,64,64])
        # e_Low = trndp.trapmf(emotional,[0,0,18,37])
        # e_Med = trndp.trimf(emotional,[34,39,44])
        # e_High = trndp.trapmf(emotional,[41,46,52,52])

        spiritual = np.arange(0,45,1)
        spi_level = {}
        spi_level["low"] = trndp.trapmf(spiritual,[0,0,13,26])
        spi_level["med"] = trndp.trimf(spiritual,[24,31,39])
        spi_level["high"] = trndp.trapmf(spiritual,[37,40,44,44])
        # sp_Low = trndp.trapmf(spiritual,[0,0,13,26])
        # sp_Med = trndp.trimf(spiritual,[24,31,39])
        # sp_High = trndp.trapmf(spiritual,[37,40,44,44])

        physical = np.arange(0,45,1)
        phy_level = {}
        phy_level["low"] = trndp.trapmf(physical,[0,0,12,25])
        phy_level["med"] = trndp.trimf(physical,[22,29,37])
        phy_level["high"] = trndp.trapmf(physical,[35,40,44,44])

        output = np.arange(0,251,1)
        out_level = {}
        out_level["vhigh"] = trndp.trapmf(output,[0,0,85,105])
        out_level["high"] = trndp.trimf(output,[90,120,155])
        out_level["med"] = trndp.trimf(output,[140,155,175])
        out_level["low"] = trndp.trimf(output,[160,180,205])
        out_level["vlow"] = trndp.trapmf(output,[180,220,227,227])

        cat_vhigh = [[0,0],[85,1],[105,0]]
        cat_high = [[90,0],[120,1],[155,0]]
        cat_med = [[140,0],[155,1],[175,0]]
        cat_low =  [[160,0],[180,1],[205,0]]
        cat_vlow = [[180,0],[220,1],[227,0]]
    else:
        # Initialize Range
        cognitive = np.arange(0, 37, 1)
        cog_level = {}
        cog_level["low"] = trndp.trapmf(cognitive, [0, 0, 13, 23])
        cog_level["med"] = trndp.trimf(cognitive, [19, 26, 33])
        cog_level["high"] = trndp.trapmf(cognitive, [32, 34, 36, 36])
        # c_Low = trndp.trapmf(cognitive,[0,0,12,24])
        # c_Med = trndp.trimf(cognitive,[20,26,33])
        # c_High = trndp.trapmf(cognitive,[32,34,36,36])

        social = np.arange(0, 53, 1)
        soc_level = {}
        soc_level["low"] = trndp.trapmf(social, [0, 0, 16, 35])
        soc_level["med"] = trndp.trimf(social, [29, 36, 45])
        soc_level["high"] = trndp.trapmf(social, [41, 46, 52, 52])
        # s_Low = trndp.trapmf(social,[0,0,16,32])
        # s_Med = trndp.trimf(social,[29,36,44])
        # s_High = trndp.trapmf(social,[41,46,52,52])

        emotional = np.arange(0, 65, 1)
        emo_level = {}
        emo_level["low"] = trndp.trapmf(emotional, [0, 0, 18, 37])
        emo_level["med"] = trndp.trimf(emotional, [34, 39, 44])
        emo_level["high"] = trndp.trapmf(emotional, [41, 46, 64, 64])
        # e_Low = trndp.trapmf(emotional,[0,0,18,37])
        # e_Med = trndp.trimf(emotional,[34,39,44])
        # e_High = trndp.trapmf(emotional,[41,46,52,52])

        spiritual = np.arange(0, 45, 1)
        spi_level = {}
        spi_level["low"] = trndp.trapmf(spiritual, [0, 0, 13, 26])
        spi_level["med"] = trndp.trimf(spiritual, [24, 31, 39])
        spi_level["high"] = trndp.trapmf(spiritual, [37, 40, 44, 44])
        # sp_Low = trndp.trapmf(spiritual,[0,0,13,26])
        # sp_Med = trndp.trimf(spiritual,[24,31,39])
        # sp_High = trndp.trapmf(spiritual,[37,40,44,44])

        physical = np.arange(0, 45, 1)
        phy_level = {}
        phy_level["low"] = trndp.trapmf(physical, [0, 0, 12, 25])
        phy_level["med"] = trndp.trimf(physical, [22, 29, 37])
        phy_level["high"] = trndp.trapmf(physical, [35, 40, 44, 44])

        output = np.arange(0, 229, 1)
        out_level = {}
        out_level["vhigh"] = trndp.trapmf(output, [0, 0, 85, 110])
        out_level["high"] = trndp.trimf(output, [90, 120, 155])
        out_level["med"] = trndp.trimf(output, [140, 155, 175])
        out_level["low"] = trndp.trimf(output, [160, 180, 200])
        out_level["vlow"] = trndp.trapmf(output, [180, 220, 228, 228])

        cat_vhigh = [[0, 0], [85, 1], [110, 0]]
        cat_high = [[90, 0], [120, 1], [155, 0]]
        cat_med = [[140, 0], [155, 1], [175, 0]]
        cat_low = [[160, 0], [180, 1], [200, 0]]
        cat_vlow = [[180, 0], [220, 1], [228, 0]]


    # fig, (aCog, aSoc, aEmo, aSpi, aPhy) = plt.subplots(nrows=5, figsize=(8, 9))
    #
    # #Cognitive Plot
    # aCog.plot(cognitive, cog_level["low"], 'r', linewidth=2, label='Low')
    # aCog.plot(cognitive, cog_level["med"], 'y', linewidth=2, label='Medium')
    # aCog.plot(cognitive, cog_level["high"], 'g', linewidth=2, label='High')
    # aCog.set_title('Cognitive')
    # aCog.legend()
    #
    # #Social Plot
    # aSoc.plot(social, soc_level["low"], 'r', linewidth=2, label='Low')
    # aSoc.plot(social, soc_level["med"], 'y', linewidth=2, label='Medium')
    # aSoc.plot(social, soc_level["high"], 'g', linewidth=2, label='High')
    # aSoc.set_title('Social')
    # aSoc.legend()
    #
    # #Emotional Plot
    # aEmo.plot(emotional, emo_level["low"], 'r', linewidth=2, label='Low')
    # aEmo.plot(emotional, emo_level["med"], 'y', linewidth=2, label='Medium')
    # aEmo.plot(emotional, emo_level["high"], 'g', linewidth=2, label='High')
    # aEmo.set_title('Emotional')
    # aEmo.legend()
    #
    # #Spiritual Plot
    # aSpi.plot(spiritual, spi_level["low"], 'r', linewidth=2, label='Low')
    # aSpi.plot(spiritual, spi_level["med"], 'y', linewidth=2, label='Medium')
    # aSpi.plot(spiritual, spi_level["high"], 'g', linewidth=2, label='High')
    # aSpi.set_title('Spiritual')
    # aSpi.legend()
    #
    # #Physical Plot
    # aPhy.plot(physical, phy_level["low"], 'r', linewidth=2, label='Low')
    # aPhy.plot(physical, phy_level["med"], 'y', linewidth=2, label='Medium')
    # aPhy.plot(physical, phy_level["high"], 'g', linewidth=2, label='High')
    # aPhy.set_title('Physical')
    # aPhy.legend()
    #
    #
    # # Turn off top/right axes
    # for ax in (aCog, aSoc, aEmo, aSpi, aPhy):
    # 	ax.spines['top'].set_visible(False)
    # 	ax.spines['right'].set_visible(False)
    # 	ax.get_xaxis().tick_bottom()
    # 	ax.get_yaxis().tick_left()
    #
    # plt.tight_layout()
    # plt.show()

    #Input Graph
    input_cog = data['cognitive']
    input_soc = data['social']
    input_emo = data['emotional']
    input_spi = data['spiritual']
    input_phy = data['physical']

    cog = {}
    cog["low"] = trndp.interp_membership(cognitive, cog_level["low"], input_cog)
    cog["med"] = trndp.interp_membership(cognitive, cog_level["med"], input_cog)
    cog["high"] = trndp.interp_membership(cognitive, cog_level["high"], input_cog)

    soc = {}
    soc["low"] = trndp.interp_membership(social, soc_level["low"], input_soc)
    soc["med"] = trndp.interp_membership(social, soc_level["med"], input_soc)
    soc["high"] = trndp.interp_membership(social, soc_level["high"], input_soc)

    emo = {}
    emo["low"] = trndp.interp_membership(emotional, emo_level["low"], input_emo)
    emo["med"] = trndp.interp_membership(emotional, emo_level["med"], input_emo)
    emo["high"] = trndp.interp_membership(emotional, emo_level["high"], input_emo)

    spi = {}
    spi["low"] = trndp.interp_membership(spiritual, spi_level["low"], input_spi)
    spi["med"] = trndp.interp_membership(spiritual, spi_level["med"], input_spi)
    spi["high"] = trndp.interp_membership(spiritual, spi_level["high"], input_spi)

    phy = {}
    phy["low"] = trndp.interp_membership(physical, phy_level["low"], input_phy)
    phy["med"] = trndp.interp_membership(physical, phy_level["med"], input_phy)
    phy["high"] = trndp.interp_membership(physical, phy_level["high"], input_phy)

    #<----- Create Rules Here ----->
    #<----- Create Rules Here ----->
    rules_vhigh = {}
    rules_vhigh["1"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_vhigh["2"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_vhigh["3"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_vhigh["4"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_vhigh["5"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_vhigh["6"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_vhigh["7"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_vhigh["8"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_vhigh["9"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_vhigh["10"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_vhigh["11"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_vhigh["12"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))

    rules_high = {}
    rules_high["1"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_high["2"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_high["3"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_high["4"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_high["5"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_high["6"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_high["7"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_high["8"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_high["9"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_high["10"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_high["11"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_high["12"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_high["13"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_high["14"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_high["15"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_high["16"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_high["17"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_high["18"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))
    rules_high["19"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_high["20"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["21"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["22"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["23"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_high["24"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_high["25"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_high["26"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_high["27"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_high["28"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["29"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_high["30"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_high["31"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_high["32"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_high["33"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_high["34"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_high["35"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_high["36"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_high["37"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_high["38"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["39"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["40"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["41"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_high["42"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_high["43"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_high["44"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_high["45"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_high["46"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["47"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_high["48"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_high["49"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_high["50"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_high["51"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_high["52"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_high["53"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_high["54"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_high["55"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_high["56"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["57"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["58"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["59"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_high["60"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_high["61"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_high["62"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_high["63"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_high["64"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["65"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_high["66"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_high["67"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_high["68"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_high["69"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_high["70"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_high["71"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_high["72"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_high["73"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_high["74"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_high["75"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["76"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["77"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["78"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_high["79"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["80"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_high["81"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_high["82"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_high["83"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["84"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["85"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_high["86"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["87"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["88"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_high["89"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["90"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["91"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["92"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_high["93"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["94"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_high["95"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_high["96"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_high["97"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_high["98"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_high["99"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_high["100"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_high["101"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_high["102"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_high["103"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["104"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["105"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["106"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_high["107"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["108"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))
    rules_high["109"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))
    rules_high["110"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["med"]))))
    rules_high["111"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))
    rules_high["112"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["low"]))))
    rules_high["113"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["low"]))))
    rules_high["114"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_high["115"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["low"]))))

    rules_med = {}
    rules_med["1"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_med["2"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_med["3"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_med["4"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_med["5"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_med["6"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_med["7"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))
    rules_med["8"] = np.fmin(cog["low"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_med["9"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_med["10"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_med["11"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_med["12"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_med["13"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_med["14"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_med["15"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))
    rules_med["16"] = np.fmin(cog["low"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_med["17"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_med["18"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_med["19"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_med["20"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_med["21"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_med["22"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_med["23"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))
    rules_med["24"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_med["25"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_med["26"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_med["27"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_med["28"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_med["29"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_med["30"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_med["31"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_med["32"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["low"]))))
    rules_med["33"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_med["34"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_med["35"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_med["36"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_med["37"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_med["38"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_med["39"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_med["40"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_med["41"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_med["42"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_med["43"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_med["44"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_med["45"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_med["46"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_med["47"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_med["48"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_med["49"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_med["50"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_med["51"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_med["52"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_med["53"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_med["54"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_med["55"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_med["56"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_med["57"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_med["58"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_med["59"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))
    rules_med["60"] = np.fmin(cog["high"], np.fmin(soc["low"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_med["61"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_med["62"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_med["63"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_med["64"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_med["65"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_med["66"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_med["67"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_med["68"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_med["69"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_med["70"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_med["71"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_med["72"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))
    rules_med["73"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["med"]))))
    rules_med["74"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["med"],phy["high"]))))
    rules_med["75"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["med"]))))
    rules_med["76"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["high"],phy["high"]))))
    rules_med["77"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["med"]))))
    rules_med["78"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["low"],phy["high"]))))
    rules_med["79"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["med"],phy["low"]))))
    rules_med["80"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["high"],phy["low"]))))
    rules_med["81"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["med"]))))
    rules_med["82"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["low"],phy["high"]))))
    rules_med["83"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["low"]))))
    rules_med["84"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["low"]))))

    rules_low = {}
    rules_low["1"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_low["2"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_low["3"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_low["4"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_low["5"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))
    rules_low["6"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_low["7"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_low["8"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_low["9"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_low["10"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_low["11"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_low["12"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_low["13"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_low["14"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_low["15"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_low["16"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_low["17"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_low["18"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))
    rules_low["19"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_low["20"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))
    rules_low["21"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_low["22"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["med"],phy["med"]))))
    rules_low["23"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_low["24"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["high"],phy["med"]))))
    rules_low["25"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["high"]))))
    rules_low["26"] = np.fmin(cog["med"], np.fmin(soc["med"], np.fmin(emo["med"],np.fmin(spi["med"],phy["med"]))))

    rules_vlow = {}
    rules_vlow["1"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_vlow["2"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_vlow["3"] = np.fmin(cog["high"], np.fmin(soc["med"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))
    rules_vlow["4"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["med"],np.fmin(spi["high"],phy["high"]))))
    rules_vlow["5"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["med"],phy["high"]))))
    rules_vlow["6"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["med"]))))


    # print(rules_vhigh["1"])
    # print(rules_high["1"])
    # print(rules_med["1"])
    # print(rules_low["1"])
    # print(rules_vlow["1"])

    #<---- Create Output ----->
    out = {}
    #Compare with
    maxVhigh = max(rules_vhigh.keys(),key=(lambda k : rules_vhigh[k]))
    out["vhigh"] = np.fmin(rules_vhigh[maxVhigh],out_level["vhigh"])

    maxHigh = max(rules_high.keys(),key=(lambda k : rules_high[k]))
    out["high"] = np.fmin(rules_high[maxHigh],out_level["high"])

    maxMed = max(rules_med.keys(),key=(lambda k : rules_med[k]))
    out["med"] = np.fmin(rules_med[maxMed],out_level["med"])

    maxLow = max(rules_low.keys(),key=(lambda k : rules_low[k]))
    out["low"] = np.fmin(rules_low[maxLow],out_level["low"])

    maxVlow = max(rules_vlow.keys(),key=(lambda k : rules_vlow[k]))
    out["vlow"] = np.fmin(rules_vlow[maxVlow],out_level["vlow"])
    # print(rules_vhigh["1"])
    # print(out_level["vhigh"])
    # print(f"VHigh = {out['vhigh']} \n")
    # #       f"High = {out['high']} \n"
    # #       f"Med = {out['med']} \n"
    # #       f"Low = {out['low']} \n"
    # #       f"Vlow = {out['vlow']} \n")
    out0 = np.zeros_like(output)
    #<------ Create Defuzzification ---->
    aggregated = np.fmax(out["vhigh"],np.fmax(out["high"],np.fmax(out["med"],np.fmax(out["low"],out["vlow"]))))
    # aggregated = out["vhigh"]

    clean_aggregated = trndp.defuzz(output,aggregated, 'centroid')
    # print(clean_aggregated)
    clean_activation = trndp.interp_membership(output,aggregated,clean_aggregated)

    fig, cAgr = plt.subplots(figsize=(8, 9))

    cAgr.plot(output, out_level["vhigh"], 'r', linewidth=2, linestyle='--', label='Very High')
    cAgr.plot(output, out_level["high"], 'y', linewidth=2, linestyle='--', label='High')
    cAgr.plot(output, out_level["med"], 'g', linewidth=2, linestyle='--', label='Medium')
    cAgr.plot(output, out_level["low"], 'k', linewidth=2, linestyle='--', label='Low')
    cAgr.plot(output, out_level["vlow"], 'b', linewidth=2, linestyle='--', label='Very Low')
    cAgr.fill_between(output, out0, aggregated, facecolor='Orange', alpha=0.7)
    cAgr.plot([clean_aggregated, clean_aggregated], [0, clean_activation], 'k', linewidth=1.5, alpha=0.9)
    cAgr.set_title('Mamdani Output')

    cAgr.legend()

    # Turn off top/right axes
    # for ax in (cAgr):
    #     ax.spines['top'].set_visible(False)
    #     ax.spines['right'].set_visible(False)
    #     ax.get_xaxis().tick_bottom()
    #     ax.get_yaxis().tick_left()

    plt.savefig("trndp_web/static/cog/"+id)
    # plt.savefig("ex_1")
    # plt.show()
    # print(aggregated)
    # print(clean_activation)
    # print(clean_aggregated)

    cog = clean_aggregated
    y = [0,0,0,0,0]
    #COG CATEGORY
    # <!-- (1) -->
    if cog <= cat_vhigh[1][0]:
        y[0] = 1
        # < !-- (2) -->
    elif cog <= cat_high[0][0]:
        m = (cat_vhigh[1][1]-cat_vhigh[2][1]) / (cat_vhigh[1][0]-cat_vhigh[2][0])
        c = -(m * cat_vhigh[2][0])
        y[0] =  m * cog + c
        # < !-- (3) -->
    elif cog <= cat_vhigh[2][0]:
        m = (cat_vhigh[1][1] - cat_vhigh[2][1]) / (cat_vhigh[1][0] - cat_vhigh[2][0])
        c = -(m * cat_vhigh[2][0])
        y[0] = m * cog + c

        m2 = (cat_high[1][1] - cat_high[0][1]) / (cat_high[1][0] - cat_high[0][0])
        c2 = -(m2 * cat_high[0][0])
        y[1] = m2 * cog + c2
        # < !-- (4) -->
    elif cog <= cat_high[1][0]:
        m = (cat_high[1][1] - cat_high[0][1]) / (cat_high[1][0] - cat_high[0][0])
        c = -(m * cat_high[0][0])
        y[1] = m * cog + c
        # < !-- (5) -->
    elif cog <= cat_med[0][0]:
        m = (cat_high[1][1]-cat_high[2][1]) / (cat_high[1][0]-cat_high[2][0])
        c = -(m * cat_high[2][0])
        y[1] =  m * cog + c
        # < !-- (6) -->
    elif cog <= cat_high[2][0]:
        m = (cat_high[2][1] - cat_high[1][1]) / (cat_high[2][0] - cat_high[1][0])
        c = -(m * cat_high[2][0])
        y[1] = m * cog + c

        m2 = (cat_med[1][1] - cat_med[0][1]) / (cat_med[1][0] - cat_med[0][0])
        c2 = -(m2 * cat_med[0][0])
        y[2] = m2 * cog + c2
        # < !-- (7) -->
    elif cog <= cat_med[1][0]:
        m2 = (cat_med[1][1] - cat_med[0][1]) / (cat_med[1][0] - cat_med[0][0])
        c2 = -(m2 * cat_med[0][0])
        y[2] = m2 * cog + c2
        # < !-- (8) -->
    elif cog <= cat_low[0][0]:
        m2 = (cat_med[1][1]-cat_med[2][1]) / (cat_med[1][0] - cat_med[2][0])
        c2 = -(m2 * cat_med[2][0])
        y[2] =  m2 * cog + c2
        # < !-- (9) --->
    elif cog <= cat_med[2][0]:
        m = (cat_med[1][1]-cat_med[2][1]) / (cat_med[1][0]-cat_med[2][0])
        c = -(m * cat_med[2][0])
        y[2] =  m * cog + c

        m2 = (cat_low[1][1]-cat_low[0][1]) / (cat_low[1][0]-cat_low[0][0])
        c2 = -(m2 * cat_low[0][0])
        y[3] =  m2 * cog + c
        # < !-- (10) -->
    elif cog <= cat_vlow[0][0]:
        m2 = (cat_low[1][1]-cat_low[0][1]) / (cat_low[1][0]-cat_low[0][0])
        c2 = -(m2 * cat_low[0][0])
        y[3] =  m2 * cog + c2
        # < !-- (11) -->
    elif cog <= cat_low[2][0]:
        m = (cat_low[1][1]-cat_low[2][1]) / (cat_low[1][0]-cat_low[2][0])
        c = -(m * cat_med[2][0])
        y[2] =  m * cog + c

        m2 = (cat_vlow[1][1]-cat_vlow[0][1]) / (cat_vlow[1][0]-cat_vlow[0][0])
        c2 = -(m2 * cat_vlow[0][0])
        y[4] =  m2 * cog + c2
        # < !-- (12) -->
    elif cog <= cat_vlow[1][0]:
        m2 = (cat_vlow[1][1]-cat_vlow[0][1]) / (cat_vlow[1][0]-cat_vlow[0][0])
        c2 = -(m2 * cat_vlow[0][0])
        y[4] =  m2 * cog + c2
    else:
        y[4] = 1

    maxIndex = np.argmax(y)
    if maxIndex == 0:
        return { "coping": "VH", "cog": cog, "y": y}
    elif maxIndex == 1:
        return { "coping": "H", "cog": cog, "y": y}
    elif maxIndex == 2:
        return { "coping": "M", "cog": cog, "y": y}
    elif maxIndex == 3:
        return { "coping": "L", "cog": cog, "y": y}
    else:
        return { "coping": "VL", "cog": cog, "y": y}
