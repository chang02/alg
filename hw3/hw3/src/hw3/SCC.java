package hw3;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class SCC {

	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		int number = Integer.parseInt(reader.readLine());
		ArrayList<String> g = new ArrayList<String>();
		for(int i=0;i<number;i++) {
			g.add(reader.readLine());
		}
		
		
	}
}
