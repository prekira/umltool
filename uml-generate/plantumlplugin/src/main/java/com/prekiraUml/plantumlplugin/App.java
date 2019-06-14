package com.prekiraUml.plantumlplugin;

import com.google.gson.Gson;
import java.io.IOException;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws IOException
    {
        System.out.println( "Hello World!" );
        
        int ver = 1;
        String jsonPath = "DtoMap"+ver+".json";
        DtoMap[] dtoList = parseJsonFromFile(jsonPath);
        //JsonObject jsonobj = new JsonObject();
        print("hello");
    }
    
    /*easier printing syntax*/
    public static void print(Object x) {
    	System.out.println(x.toString());
    }
    
    
    public static DtoMap[] parseJsonFromFile(String filename) {
        Gson gson = new Gson();
        return gson.fromJson(Data.getFileContentsAsString(filename), DtoMap[].class);
    }
}
