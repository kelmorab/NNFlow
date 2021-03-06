from __future__ import absolute_import, division, print_function




def generator_level_variables():

    generator_level_variables_list = ['GenHiggs_DecProd1_Eta',
                                      'GenHiggs_DecProd1_PDGID',
                                      'GenHiggs_DecProd1_Pt',
                                      'GenHiggs_DecProd2_Eta',
                                      'GenHiggs_DecProd2_PDGID',
                                      'GenHiggs_DecProd2_Pt',
                                      'GenHiggs_Eta',
                                      'GenHiggs_Phi',
                                      'GenHiggs_Pt',
                                      'Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX',
                                      'Prescale_HLT_IsoMu24_vX',
                                      'Prescale_HLT_IsoTkMu24_vX',
                                      'Evt_ID',
                                      'Evt_Odd',
                                      'Evt_Lumi',
                                      'Evt_Run',
                                      'Evt_Phi_GenMET',
                                      'Evt_Pt_GenMET',
                                      'GenEvt_TTxId_FromProducer',
                                      'N_GenTopHad',
                                      'N_GenTopLep',
                                      'N_GoodTags',
                                      'N_GoodTagsM',
                                      'N_MisTags',
                                      'N_MisTagsM',
                                      'N_TotalTags',
                                      'GenEvt_I_TTPlusBB',
                                      'GenEvt_I_TTPlusCC',
                                      'TTBB_GenEvt_I_TTPlusBB',
                                      'TTBB_GenEvt_I_TTPlusCC',
                                      'TTBB_GenEvt_TTxId_FromProducer',
                                      'Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX',
                                      'Triggered_HLT_IsoMu24_vX',
                                      'Triggered_HLT_IsoTkMu24_vX',
                                      'GenTopHad_Eta',
                                      'GenTopHad_Phi',
                                      'GenTopHad_Pt',
                                      'GenTopLep_Eta',
                                      'GenTopLep_Phi',
                                      'GenTopLep_Pt',
                                      'Jet_GenJet_Eta',
                                      'Jet_GenJet_Pt',
                                      'Jet_Flav',
                                      'Jet_PartonFlav',
                                      'Jet_PileUpID',
                                      'Reco_highest_TopAndWHadLikelihood',
                                      'Reco_existingAll',
                                      'Reco_existingH',
                                      'Reco_existingN',
                                      'Reco_existingW',
                                      'Reco_foundAll_with_TTBBLikelihood',
                                      'Reco_foundAll_with_TTBBLikelihoodTimesME',
                                      'Reco_foundAll_with_TTHLikelihood',
                                      'Reco_foundAll_with_TTHLikelihoodTimesME',
                                      'Reco_foundAll_with_TTLikelihood',
                                      'Reco_foundAll_with_TTLikelihood_comb',
                                      'Reco_foundH_with_TTBBLikelihood',
                                      'Reco_foundH_with_TTBBLikelihoodTimesME',
                                      'Reco_foundH_with_TTHLikelihood',
                                      'Reco_foundH_with_TTHLikelihoodTimesME',
                                      'Reco_foundH_with_TTLikelihood',
                                      'Reco_foundH_with_TTLikelihood_comb',
                                      'Reco_foundN_with_TTBBLikelihood',
                                      'Reco_foundN_with_TTBBLikelihoodTimesME',
                                      'Reco_foundN_with_TTHLikelihood',
                                      'Reco_foundN_with_TTHLikelihoodTimesME',
                                      'Reco_foundN_with_TTLikelihood',
                                      'Reco_foundN_with_TTLikelihood_comb',
                                      'Reco_foundW_with_TTBBLikelihood',
                                      'Reco_foundW_with_TTBBLikelihoodTimesME',
                                      'Reco_foundW_with_TTHLikelihood',
                                      'Reco_foundW_with_TTHLikelihoodTimesME',
                                      'Reco_foundW_with_TTLikelihood',
                                      'Reco_foundW_with_TTLikelihood_comb',
                                      'Reco_highest_TTHLikelihoodTimesME',
                                      'Reco_highest_TTLikelihood',
                                      'Reco_highest_TTHLikelihood',
                                      'Reco_highest_TTBBLikelihood',
                                      'Reco_highest_TTBBLikelihoodTimesME',
                                      'Reco_highest_TTLikelihood_comb',
                                      'Gen_highest_TopAndWHadLikelihood',
                                      'Gen_existingAll',
                                      'Gen_existingH',
                                      'Gen_existingN',
                                      'Gen_existingW',
                                      'Gen_foundAll_with_TTBBLikelihood',
                                      'Gen_foundAll_with_TTBBLikelihoodTimesME',
                                      'Gen_foundAll_with_TTHLikelihood',
                                      'Gen_foundAll_with_TTHLikelihoodTimesME',
                                      'Gen_foundAll_with_TTLikelihood',
                                      'Gen_foundAll_with_TTLikelihood_comb',
                                      'Gen_foundH_with_TTBBLikelihood',
                                      'Gen_foundH_with_TTBBLikelihoodTimesME',
                                      'Gen_foundH_with_TTHLikelihood',
                                      'Gen_foundH_with_TTHLikelihoodTimesME',
                                      'Gen_foundH_with_TTLikelihood',
                                      'Gen_foundH_with_TTLikelihood_comb',
                                      'Gen_foundN_with_TTBBLikelihood',
                                      'Gen_foundN_with_TTBBLikelihoodTimesME',
                                      'Gen_foundN_with_TTHLikelihood',
                                      'Gen_foundN_with_TTHLikelihoodTimesME',
                                      'Gen_foundN_with_TTLikelihood',
                                      'Gen_foundN_with_TTLikelihood_comb',
                                      'Gen_foundW_with_TTBBLikelihood',
                                      'Gen_foundW_with_TTBBLikelihoodTimesME',
                                      'Gen_foundW_with_TTHLikelihood',
                                      'Gen_foundW_with_TTHLikelihoodTimesME',
                                      'Gen_foundW_with_TTLikelihood',
                                      'Gen_foundW_with_TTLikelihood_comb',
                                      'Gen_highest_TTBBLikelihood',
                                      'Gen_highest_TTBBLikelihoodTimesME',
                                      'Gen_highest_TTHLikelihood',
                                      'Gen_highest_TTHLikelihoodTimesME',
                                      'Gen_highest_TTLikelihood',
                                      'Gen_highest_TTLikelihood_comb']


    return generator_level_variables_list




def other_always_excluded_variables():


    other_always_excluded_variables_list = ['HadTop_B_additionalTaggedJets',
                                            'HadTop_B_additionalUntaggedJets',
                                            'HadTop_W1_additionalTaggedJets',
                                            'HadTop_W1_additionalUntaggedJets',
                                            'HadTop_W2_additionalTaggedJets',
                                            'HadTop_W2_additionalUntaggedJets',
                                            'HadTop_W_additionalTaggedJets',
                                            'HadTop_W_additionalUntaggedJets',
                                            'HadTop_additionalTaggedJets',
                                            'HadTop_additionalUntaggedJets',
                                            'LepTop_B_additionalTaggedJets',
                                            'LepTop_B_additionalUntaggedJets',
                                            'LepTop_W1_additionalTaggedJets',
                                            'LepTop_W1_additionalUntaggedJets',
                                            'LepTop_W2_additionalTaggedJets',
                                            'LepTop_W2_additionalUntaggedJets',
                                            'LepTop_W_additionalTaggedJets',
                                            'LepTop_W_additionalUntaggedJets',
                                            'LepTop_additionalTaggedJets',
                                            'LepTop_additionalUntaggedJets',
                                            'Muon_Charge',
                                            'Muon_E',
                                            'Muon_Eta',
                                            'Muon_M',
                                            'Muon_Phi',
                                            'Muon_Pt',
                                            'Muon_RelIso',
                                            'Electron_Charge',
                                            'Electron_E',
                                            'Electron_Eta',
                                            'Electron_M',
                                            'Electron_Phi',
                                            'Electron_Pt',
                                            'Electron_RelIso',
                                            'Evt_Pt_PrimaryLepton',
                                            'Evt_Eta_PrimaryLepton',
                                            'Evt_Phi_PrimaryLepton',
                                            'Evt_M_PrimaryLepton',
                                            'Evt_E_PrimaryLepton',
                                            'BDT_common5_input_avg_btag_disc_btags',
                                            'BDT_common5_input_dev_from_avg_disc_btags',
                                            'BDT_common5_input_maxeta_jet_tag',
                                            'BDT_common5_input_maxeta_tag_tag',
                                            'BDT_common5_input_maxeta_jet_jet',
                                            'BDT_common5_input_blr_transformed',
                                            'BDT_common5_input_min_dr_tagged_jets',
                                            'BDT_common5_input_MET',
                                            'BDT_common5_input_M3',
                                            'BDT_common5_input_HT',
                                            'BDT_common5_input_MHT',
                                            'BDT_common5_input_Evt_M_MinDeltaRTaggedJets',
                                            'BDT_common5_input_Evt_Deta_JetsAverage',
                                            'BDT_common5_input_Evt_Deta_TaggedJetsAverage',
                                            'BDT_common5_input_Evt_CSV_Average',
                                            'BDT_common5_input_second_highest_btag',
                                            'BDT_common5_input_third_highest_btag',
                                            'BDT_common5_input_fourth_highest_btag',
                                            'BDT_common5_input_fifth_highest_CSV',
                                            'BDT_common5_input_first_jet_pt',
                                            'BDT_common5_input_second_jet_pt',
                                            'BDT_common5_input_third_jet_pt',
                                            'BDT_common5_input_fourth_jet_pt',
                                            'BDT_common5_output',
                                            'Evt_Dr_TaggedJetsAverage',
                                            'Evt_M_MinDeltaRLeptonTaggedJet'
                                            'Evt_Aplanarity',
                                            'Evt_Sphericity']


    return other_always_excluded_variables_list
