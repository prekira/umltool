package com.prekiraUml.plantumlplugin;


import java.io.IOException;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Hello world!
 *
 */
public class App 
{
	public static String[] stereotypes = {"Audited", "interface", "enumeration"};
    public static String[] classNamesToIgnore = {"Dto", "String", "Boolean"};
    
	
	public static void main( String[] args ) throws IOException
    {
        System.out.println( "Hello World!" );
        JSONObject dtoMap = parseJson();
        
        //String pageName = dtoMap.getJSONObject("pageInfo").getString("pageName");
        JSONArray dtoList = (dtoMap.getJSONArray("data"));
        print(dtoList.getJSONObject(0).getString("className"));
    }
	
	public String getPropertiesFromDto(JSONObject dto) {
		String propertyOfClass = "\n{\n";
		String connectionsOfClass = "";
		JSONArray propertyList = dto.getJSONArray("properties");
		for (int i = 0; i < propertyList.length(); i++) {
			propertyOfClass += "	+";
			
			
		}
	}
	
	/**
	 * find if dtoobject is dto from type name
	 * @param typeName full type name
	 * @return if obj is dto
	 */
	public boolean isDto(String typeName) {
		return typeName.substring(typeName.lastIndexOf(".") - "dto".length(), typeName.lastIndexOf(".")).toLowerCase().equals("dto");
	}
	
	/**
	 * extract class name from string of package directory
	 * @param name of path
	 * @return name of individual class
	 */
	public String getClassNameFromString(String name) {
		return name.substring(name.lastIndexOf(".")+1, name.length()); 
	}
    
	public String getStereotypeFromDto(JSONObject dto) {
		JSONArray stereotypeList = dto.getJSONArray("annotations");
		for (int i; i < stereotypeList.length(); i++) {
			
		}
	}
	
    /*easier printing syntax*/
    public static void print(Object x) {
    	System.out.println(x.toString());
    }
    
    public static JSONObject parseJson() {
    	int ver = 1;
        String jsonPath = "DtoMap"+ver+".json";
        return new JSONObject("{ \"data\": " + Data.getFileContentsAsString(jsonPath) + "}");
    }
}
