if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException, UsernameException
    from httplib import HTTPException

    from CRABClient.UserUtilities import config, getUsername
    config = config()

    config.General.workArea = 'HeavyIon_Forest_ZB7'
    config.General.transferOutputs = True
    config.General.transferLogs = False
    config.JobType.pluginName = 'Analysis'
    #config.JobType.numCores = 1
    #config.JobType.maxMemoryMB = 2500
    config.JobType.maxJobRuntimeMin = 2700
    config.JobType.maxMemoryMB = 4000
    config.JobType.allowUndistributedCMSSW = True
    config.JobType.inputFiles = ['HeavyIonRPRcd_pPb2016_MB_offline.db','offset_pPb2016_Pbp_MB.root']
    config.Data.splitting = 'FileBased'
    config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
    config.Data.unitsPerJob = 1 ###files per job (but not impose)
    config.Data.totalUnits = 443 ###how many files to analyze
    config.Data.inputDBS = 'global'
    config.Data.outLFNDirBase = '/store/user/%s/' % (getUsername())
    #config.Data.outLFNDirBase = "/store/group/phys_heavyions/%s/gamma_pomeron_files" % (getUsername())
    config.Data.publication = False
    #config.Data.ignoreLocality = True
    config.Site.storageSite = 'T2_US_Nebraska'
    #config.Site.whitelist = ['T2_US_Vanderbilt']

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
            
    config.JobType.psetName = 'runForestAOD_pPb_DATA_80X.py'

    config.General.requestName = 'HeavyIon_Forest_pPb_8p16TeV_pgoing_ZB_PD7'
    config.Data.inputDataset = '/PAZeroBias7/PARun2016C-PromptReco-v1/AOD'
    #config.Data.lumiMask = 'Cert_285952-286496_HI8TeV_PromptReco_Pbp_Collisions16_JSON_NoL1T.txt'
    config.Data.runRange ='286204,286303,286311'
    config.Data.outputDatasetTag = 'HeavyIon_Forest_pPb_8p16TeV_pgoing_ZB_PD7'
    submit(config)

