/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.herry.sdudy;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map.Entry;

/**
 *
 * @author xuegao
 */
public class JDKSdudy {
    private    List l = new ArrayList();
    
    public static void main(String args[]) throws IOException{
        System.err.println("ERROR");
        
        for(Entry<String,String> e:System.getenv().entrySet()){
        
            System.out.println(e.getKey()+"==>"+e.getValue());
        }
        ArrayList al = new ArrayList();
        
    }    
   
}
