################################################################
## In principle all you have to setup is defined in this file ##
################################################################

from configManager import configMgr
from ROOT import kBlack,kWhite,kGray,kRed,kPink,kMagenta,kViolet,kBlue,kAzure,kCyan,kTeal,kGreen,kSpring,kYellow,kOrange
from configWriter import TopLevelXML,Measurement,ChannelXML,Sample
from systematic import Systematic

from ROOT import gROOT
gROOT.LoadMacro("./macros/AtlasStyle.C")
import ROOT
ROOT.SetAtlasStyle()

#gROOT.ProcessLine("gErrorIgnoreLevel=10001;")
#gROOT.SetBatch(False)
#configMgr.plotHistos = True

rel17=True

useStat=True

# First define HistFactory attributes
configMgr.analysisName = "MyOneLeptonKtScaleFit_discoveryUpperLimit"

# Scaling calculated by outputLumi / inputLumi
configMgr.inputLumi = 1.917  # Luminosity of input TTree after weighting
configMgr.outputLumi = 1.917   # Luminosity required for output histograms
configMgr.setLumiUnits("fb-1")

if rel17:
    configMgr.inputLumi = 0.001
    configMgr.outputLumi = 4.713 #1.917   # Luminosity required for output histograms
    configMgr.analysisName+="R17" 

configMgr.outputFileName = "results/"+configMgr.analysisName+"_Output.root"


# setting the parameters of the hypothesis test
#configMgr.doHypoTest=False
#configMgr.nTOYs=1000
#configMgr.calculatorType=0
#configMgr.testStatType=3
#configMgr.nPoints=20

# Set the files to read from
if configMgr.readFromTree:
    if rel17:
        configMgr.inputFileNames = []
        configMgr.inputFileNames.append("samples/SusyFitterTree_OneEle_Rel17_BG_Syst.root")
        configMgr.inputFileNames.append("samples/SusyFitterTree_OneMu_Rel17_BG_Syst.root")
        configMgr.inputFileNames.append("samples/SusyFitterTree_p832_mSUGRA_v3.root")
    else:
        configMgr.inputFileNames = ["samples/SusyFitterTree_OneEle.root","samples/SusyFitterTree_OneMu.root"]
else:
    configMgr.inputFileNames = ["data/"+configMgr.analysisName+".root"]

# Dictionnary of cuts for Tree->hist
configMgr.cutsDict["WR"] = "lep2Pt<10 && met>30 && met<120 && mt>40 && mt<80 && nB3Jet==0 && jet1Pt>80 && jet3Pt>25 && meffInc>400"
configMgr.cutsDict["TR"] = "lep2Pt<10 && met>30 && met<120 && mt>40 && mt<80 && nB3Jet>0 && jet1Pt>80 && jet3Pt>25 && meffInc>400"
configMgr.cutsDict["VR"] = "lep2Pt<10 && met>120 && met<250 && mt>80 && jet1Pt>80 && jet3Pt>25 && meffInc>400"
configMgr.cutsDict["VR2"] = "lep2Pt<10 && met<250 && mt>80 && jet1Pt>80 && jet3Pt>25 && meffInc>400"
configMgr.cutsDict["S3"] = "lep2Pt<10 && met>250 && mt>100 && met/meff3Jet>0.3 && jet1Pt>100 && jet3Pt>25 && jet4Pt<80"
configMgr.cutsDict["S4"] = "lep2Pt<10 && met>250 && mt>100 && met/meff4Jet>0.2 && jet4Pt>80"
configMgr.cutsDict["SS"] = "lep2Pt<10 && met>250 && mt>100 && jet1Pt>120 && jet2Pt>25"

d=configMgr.cutsDict
configMgr.cutsDict["SR3jT"] = d["S3"]+"&& meffInc>1200"
configMgr.cutsDict["SR4jT"] = d["S4"]+"&& meffInc>800"
configMgr.cutsDict["SR1s2j"] = d["SS"]+"&& met/meffInc>0.3"

# Dictionnary of cuts for Tree->hist in MeV
cutsDictMeV = {}
cutsDictMeV["WR"] = "lep2Pt<10000 && met>30000 && met<120000 && mt>40000 && mt<80000 && nB3Jet==0 && jet1Pt>80000 && jet3Pt>25000 && meffInc>400000"
cutsDictMeV["TR"] = "lep2Pt<10000 && met>30000 && met<120000 && mt>40000 && mt<80000 && nB3Jet>0 && jet1Pt>80000 && jet3Pt>25000 && meffInc>400000"
cutsDictMeV["VR"] = "lep2Pt<10000 && met>120000 && met<250000 && mt>80000 && jet1Pt>80000 && jet3Pt>25000 && meffInc>400000"
cutsDictMeV["VR2"] = "lep2Pt<10000 && met<250000 && mt>80000 && jet1Pt>80000 && jet3Pt>25000 && meffInc>400000"
cutsDictMeV["S3"] = "lep2Pt<10000 && met>250000 && mt>100000 && met/meff3Jet>0.3 && jet1Pt>100000 && jet3Pt>25000 && jet4Pt<80000"
cutsDictMeV["S4"] = "lep2Pt<10000 && met>250000 && mt>100000 && met/meff4Jet>0.2 && jet4Pt>80000"
cutsDictMeV["SS"] = "lep2Pt<10000 && met>250000 && mt>100000 && jet1Pt>120000 && jet2Pt>25000"

d=cutsDictMeV
cutsDictMeV["SR3jT"] = d["S3"]+"&& meffInc>1200000"
cutsDictMeV["SR4jT"] = d["S4"]+"&& meffInc>800000"
cutsDictMeV["SR1s2j"] = d["SS"]+"&& met/meffInc>0.3"

# Tuples of nominal weights without and with b-jet selection
configMgr.weights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","bTagWeight3Jet")

xsecSigHighWeights = ("genWeightUp","eventWeight","leptonWeight","triggerWeight","truthWptWeight","bTagWeight3Jet")
xsecSigLowWeights = ("genWeightDown","eventWeight","leptonWeight","triggerWeight","truthWptWeight","bTagWeight3Jet")

# For weight-based systematic
ktScaleWHighWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ktfacUpWeightW","bTagWeight3Jet")
ktScaleWLowWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ktfacDownWeightW","bTagWeight3Jet")

ktScaleTopHighWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ktfacUpWeightTop","bTagWeight3Jet")
ktScaleTopLowWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ktfacDownWeightTop","bTagWeight3Jet")

ptMinTopHighWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ptmin20WeightTop","bTagWeight3Jet")
ptMinTopLowWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ptmin20WeightTop","bTagWeight3Jet")

ptMinWZHighWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ptmin20WeightW","bTagWeight3Jet")
ptMinWZLowWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","ptmin20WeightW","bTagWeight3Jet")

bTagHighWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","bTagWeight3JetHigh")
bTagLowWeights = ("genWeight","eventWeight","leptonWeight","triggerWeight","truthWptWeight","bTagWeight3JetLow")

# QCD weights without and with b-jet selection
configMgr.weightsQCD = "qcdWeight"
configMgr.weightsQCDWithB = "qcdBWeight"

# List of systematics
topKtScale = Systematic("KtScaleTop",configMgr.weights,ktScaleTopHighWeights,ktScaleTopLowWeights,"weight","histoSys")
wzKtScale = Systematic("KtScaleWZ",configMgr.weights,ktScaleWHighWeights,ktScaleWLowWeights,"weight","histoSys")

topPtMin = Systematic("PtMinTop",configMgr.weights,ptMinTopHighWeights,ptMinTopLowWeights,"weight","histoSys")
wzPtMin = Systematic("PtMinWZ",configMgr.weights,ptMinWZHighWeights,ptMinWZLowWeights,"weight","histoSys")

xsecSig = Systematic("XSS",configMgr.weights,xsecSigHighWeights,xsecSigLowWeights,"weight","overallSys")

jesWR = Systematic("JW","_NoSys","_JESup","_JESdown","tree","histoSys")
jesTR = Systematic("JT","_NoSys","_JESup","_JESdown","tree","histoSys")
jesS3 = Systematic("J3","_NoSys","_JESup","_JESdown","tree","histoSys")
jesS4 = Systematic("J4","_NoSys","_JESup","_JESdown","tree","histoSys")

jesSR = Systematic("JS","_NoSys","_JESup","_JESdown","tree","histoSys")
jesTopSR = Systematic("JTS","_NoSys","_JESup","_JESdown","tree","histoSys")
jesWZSR = Systematic("JWZS","_NoSys","_JESup","_JESdown","tree","histoSys")
jesSIGSR = Systematic("JSS","_NoSys","_JESup","_JESdown","tree","histoSys")

jesCR = Systematic("JC","_NoSys","_JESup","_JESdown","tree","shapeSys")

jesTop = Systematic("JT","_NoSys","_JESup","_JESdown","tree","histoSys")
jesWZ = Systematic("JW","_NoSys","_JESup","_JESdown","tree","histoSys")
jesSig = Systematic("JS","_NoSys","_JESup","_JESdown","tree","histoSys")
jesBG = Systematic("JB","_NoSys","_JESup","_JESdown","tree","histoSys")

jes = Systematic("JES","_NoSys","_JESup","_JESdown","tree","histoSys")

configMgr.nomName = "_NoSys"

# List of samples and their plotting colours
topSample = Sample("Top",kGreen-9)
topSample.setNormFactor("mu_Top",1.,0.,5.)
topSample.setStatConfig(useStat)
#topSample.addSystematic(jesTop)
wzSample = Sample("WZ",kAzure+1)
wzSample.setNormFactor("mu_WZ",1.,0.,5.)
wzSample.setStatConfig(useStat)
#wzSample.addSystematic(jesWZ)
bgSample = Sample("BG",kYellow-3)
bgSample.setNormFactor("mu_BG",1.,0.,5.)
bgSample.setStatConfig(useStat)
#bgSample.addSystematic(jesBG)
qcdSample = Sample("QCD",kGray+1)
qcdSample.setQCD(True,"histoSys")
qcdSample.setStatConfig(useStat)
dataSample = Sample("Data",kBlack)
dataSample.setData()

#Binnings
nJetBinLow = 3
nJetBinHighTR = 10
nJetBinHighWR = 10

nBJetBinLow = 0
nBJetBinHigh = 4

meffNBins = 6
meffBinLow = 400.
meffBinHigh = 1600.

lepPtNBins = 6
lepPtLow = 20.
lepPtHigh = 600.

srNBins = 1
srBinLow = 0.5
srBinHigh = 1.5

#------------
#Bkg only fit
#------------

bkt = configMgr.addTopLevelXML("BkgOnlyKt")
if useStat:
    bkt.statErrThreshold=0.03
else:
    bkt.statErrThreshold=None
bkt.addSamples([topSample,wzSample,qcdSample,bgSample,dataSample])
bkt.getSample("Top").addSystematic(topKtScale)
bkt.getSample("WZ").addSystematic(wzKtScale)
#bkt.getSample("Top").addSystematic(topPtMin)
#bkt.getSample("WZ").addSystematic(wzPtMin)

meas=bkt.addMeasurement(name="NormalMeasurement",lumi=1.0,lumiErr=0.039)
meas.addPOI("mu_SIG")
meas.addParamSetting("mu_BG",True,1)

#CRs
nJetW = bkt.addChannel("nJet",["WR"],nJetBinHighWR-nJetBinLow,nJetBinLow,nJetBinHighWR)
nJetW.hasB = True
nJetW.addSystematic(jesCR)
nJetT = bkt.addChannel("nJet",["TR"],nJetBinHighTR-nJetBinLow,nJetBinLow,nJetBinHighTR)
nJetT.hasB = True
nJetT.addSystematic(jesCR)
#bkt.addSystematic(jes)
bkt.setBkgConstrainChannels([nJetW,nJetT])

#VRs
nJetVR = bkt.addChannel("nJet",["VR"],nJetBinHighTR-nJetBinLow,nJetBinLow,nJetBinHighTR)
nBJetVR = bkt.addChannel("nBJet",["VR"],nBJetBinHigh-nBJetBinLow,nBJetBinLow,nBJetBinHigh)
meffVR = bkt.addChannel("meffInc",["VR"],meffNBins,meffBinLow,meffBinHigh) 
metVR = bkt.addChannel("met",["VR2"],6,30,250)
bkt.setValidationChannels([nJetVR,nBJetVR,meffVR,metVR]) #These are not necessarily statistically independent

#SRs
#meff3J = bkt.addChannel("meffInc",["S3"],meffNBins,meffBinLow,meffBinHigh)
#meff3J.addSystematic(jesS3)
#meff3J.useOverflowBin=True
#meff4J = bkt.addChannel("meffInc",["S4"],meffNBins,meffBinLow,meffBinHigh) 
#meff4J.addSystematic(jesS4)
#meff4J.useOverflowBin=True
#bkt.setBkgConstrainChannels([nJetW,nJetT,meff3J,meff4J])

#--------------
# Discovery fit
#--------------
discovery = configMgr.addTopLevelXML("Discovery")
if useStat:
    discovery.statErrThreshold=0.03
else:
    discovery.statErrThreshold=None
discovery.addSamples([topSample,wzSample,qcdSample,bgSample,dataSample])
discovery.getSample("Top").addSystematic(topKtScale)
discovery.getSample("WZ").addSystematic(wzKtScale)
#discovery.getSample("Top").addSystematic(topPtMin)
#discovery.getSample("WZ").addSystematic(wzPtMin)

measD=discovery.addMeasurement(name="DiscoveryMeasurement",lumi=1.0,lumiErr=0.039)
measD.addPOI("mu_SR3jT")
measD.addParamSetting("mu_BG",True,1)

#CRs
nJetW = discovery.addChannel("nJet",["WR"],nJetBinHighWR-nJetBinLow,nJetBinLow,nJetBinHighWR)
nJetW.hasB = True
nJetW.addSystematic(jesCR)
nJetT = discovery.addChannel("nJet",["TR"],nJetBinHighTR-nJetBinLow,nJetBinLow,nJetBinHighTR)
nJetT.hasB = True
nJetT.addSystematic(jesCR)
#discovery.addSystematic(jes)
discovery.setBkgConstrainChannels([nJetW,nJetT])
###
sr3jTChannel = discovery.addChannel("cuts",["SR3jT"],srNBins,srBinLow,srBinHigh)
sr4jTChannel = discovery.addChannel("cuts",["SR4jT"],srNBins,srBinLow,srBinHigh)
#s3Channel = discovery.addChannel("cuts",["S3"],srNBins,srBinLow,srBinHigh)
#s4Channel = discovery.addChannel("cuts",["S4"],srNBins,srBinLow,srBinHigh)
## sr3jTChannel.addSystematic(jesSR)
## sr4jTChannel.addSystematic(jesSR)
## s3Channel.addSystematic(jesSR)
## s4Channel.addSystematic(jesSR)
sr3jTChannel.addDiscoverySamples(["SR3jT"],[1.],[0.],[10.],[kMagenta])
sr4jTChannel.addDiscoverySamples(["SR4jT"],[1.],[0.],[10.],[kMagenta])
#s3Channel.addDiscoverySamples(["S3"],[1.],[-100.],[100.],[kMagenta])
#s4Channel.addDiscoverySamples(["S4"],[1.],[-100.],[100.],[kMagenta])
discovery.setSignalChannels( [sr3jTChannel,sr4jTChannel])
#srChannel.addDiscoverySamples(["S3","S4"],[1.,1.],[-10.,-10.],[10.,10.],[kBlue,kBlue])
#srChannel = discovery.addChannel("cuts",["S3","S4"],srNBins,srBinLow,srBinHigh)
#srChannel.addSystematic(jesSR)
#srChannel.addDiscoverySamples(["S3","S4"],[1.,1.],[-20.,-20.],[20.,20.],[kBlue,kBlue])
#discovery.setSignalChannels(srChannel)

## #-----------------------------
## # Exclusion fits (MSUGRA grid)
## #-----------------------------

## sigSamples=["SU_180_360","SU_580_240","SU_740_330","SU_900_420","SU_1300_210"]
## if rel17:
##     sigSamples=["SU_580_240_0_10_P"]
## for sig in sigSamples:
##     myTopLvl = configMgr.addTopLevelXMLClone(bkt,"Sig_%s"%sig)
##     myTopLvl.getMeasurement("NormalMeasurement").addConstraintTerm("XSS","Gamma",0.3)
##     sigSample = Sample(sig,kPink)
##     sigSample.setNormByTheory()
##     sigSample.setStatConfig(useStat)
##     sigSample.setNormFactor("mu_SIG",1.,0.,5.)
##     #sigSample.addSystematic(jesSig)
##     sigSample.addSystematic(xsecSig)
##     sigSample.setCutsDict(cutsDictMeV)
##     sigSample.setUnit("MeV")
##     myTopLvl.addSamples(sigSample)
##     myTopLvl.setSignalSample(sigSample)
##     meff3J = myTopLvl.addChannel("meffInc",["S3"],meffNBins,meffBinLow,meffBinHigh) 
##     meff3J.useOverflowBin=True
##  ##  meff3J.addSystematic(jesSR)
##     meff3J.addSystematic(jesSIGSR)
##     meff3J.getSample("Top").addSystematic(jesTopSR)
##     meff3J.getSample("BG").addSystematic(jesTopSR) # this is not a typo, we use the jesTop for both Top and single-top(=BG)
##     meff3J.getSample("WZ").addSystematic(jesWZSR)
##     meff4J = myTopLvl.addChannel("meffInc",["S4"],meffNBins,meffBinLow,meffBinHigh)
##     meff4J.useOverflowBin=True
##  ##   meff4J.addSystematic(jesSR)
##     meff4J.addSystematic(jesSIGSR)
##     meff4J.getSample("Top").addSystematic(jesTopSR)
##     meff4J.getSample("BG").addSystematic(jesTopSR) # this is not a typo, we use the jesTop for both Top and single-top(=BG)
##     meff4J.getSample("WZ").addSystematic(jesWZSR)
##     myTopLvl.setSignalChannels([meff3J,meff4J])
