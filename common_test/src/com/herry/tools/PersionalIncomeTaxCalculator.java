package com.herry.tools;

public class PersionalIncomeTaxCalculator {
        //新版个税起征点
	private static double newNoneTaxIncomeBase =3500;
        //新版交税区间及税率
        private static double[] newNeedTaxMountByLevel = new double[]{0,1500,4500,9000,35000,55000,80000};
	private static float[] newTaxRat = new float[]{0.03f,0.1f,0.2f,0.25f,0.3f,0.35f,0.45f};
	
        //旧版个税起征点
	private static double noneTaxIncomeBase =2000;
        //旧交税区间及税率
	private static double[] needTaxMountByLevel = new double[]{0,500,2000,5000,20000,40000,60000,80000,100000};
	private static float[] taxRat = new float[]{0.05f,0.1f,0.15f,0.2f,0.25f,0.3f,0.35f,0.4f,0.45f};
	
	
	private static double base = 12000;      //基本工资
	private static double addtoBase = 500+2400;  //福利津贴
        private static double sheBaoBase = 2338; //社保基数
	private static double  sheBao = 140.22f+base*0.07;//社保，公积金
	
	public static void main(String args[]){
		
		
		double eat01 = 270.97;
		double eat02 =264.00;
		double eatAdd = 0;//饭贴
		double endGet = 0;
		double sumBeforTax = 0;
		
		//http://ess.sh.pegatroncorp.com/ess/redirect.php?scriptname=ESS0000
		
		double taxMount =0;
		double getMount =0;
		double totalIncomBeforSheBao=base+addtoBase+eatAdd ;
		
		double totalIncomSubShebao=base+addtoBase+eatAdd-sheBao ;
		
		double needTaxMount = totalIncomSubShebao -noneTaxIncomeBase; 
		/*
                 //旧版
		if(needTaxMountByLevel.length==taxRat.length){
			double a = 0;
			double b = 0;
			
			for(int i=needTaxMountByLevel.length-1;i>=0;i--){
				a = needTaxMount-needTaxMountByLevel[i];
				b = taxRat[i];
				if(a>0){
					taxMount +=(a*b);
					needTaxMount =  needTaxMountByLevel[i];
				}
			}
		}
		endGet = totalIncomSubShebao -taxMount;
		System.out.println("By Old~~ totalIncom:"+totalIncomSubShebao+";taxMount:"+taxMount+";getMount:"+(totalIncomSubShebao-taxMount));
		*/
                //新标准
		taxMount =0 ;
		needTaxMount = totalIncomSubShebao -newNoneTaxIncomeBase; 
		if(newNeedTaxMountByLevel.length==newTaxRat.length){
			double a = 0;
			double b = 0;
			
			for(int i=newNeedTaxMountByLevel.length-1;i>=0;i--){
				a = needTaxMount-newNeedTaxMountByLevel[i];
				b = newTaxRat[i];
				if(a>0){
					taxMount +=(a*b);
					needTaxMount =  newNeedTaxMountByLevel[i];
				}
			}
		}
		
		endGet = totalIncomSubShebao -taxMount;
		
		System.out.println("By New~~\nbase="+base+"\naddtoBase="+addtoBase+";\nSheBao="+sheBao+"\neat01="+eat01+"\teat02="+eat02+"\teatAdd="+eatAdd+";\ntotalIncomBeforSheBao="+totalIncomBeforSheBao+"\ttotalIncomSubShebao="+totalIncomSubShebao+"\ttaxMount="+taxMount+";\tgetMount="+endGet);
	}
}
