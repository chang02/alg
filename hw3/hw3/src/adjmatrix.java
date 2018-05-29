import java.util.ArrayList;

public class adjmatrix {
	public adjmatrix(ArrayList<String> g) {
		int[][] m = new int[g.size()][g.size()];
		for(int i=0;i<g.size();i++) {
			for(int j=0;j<g.size();j++) {
				m[i][j] = 0;
			}
		}
		for(int i=0;i<g.size();i++) {
			String[] line_arr = g.get(i).split(" ");
			int number = Integer.parseInt(line_arr[0]);
			for(int j=0;j<number;j++) {
				m[i][Integer.parseInt(line_arr[j+1])] = 1;
			}
		}
	}
}
