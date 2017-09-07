package ca.uqac.lif.labpalJython;

import java.net.URL;
import org.python.util.jython;


public class Runner 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		//
		URL pyUrl = Runner.class.getResource("/__main__.py");
		String jarPath=pyUrl.getPath().replace("!/__main__.py", "");
		jarPath = jarPath.replace("file:", "");
		String jythonInput[] = {jarPath};
		jython.run(jythonInput);

	}

}
