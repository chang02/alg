import java.util.ArrayList;
import java.util.LinkedList;
public class adjlist {
	LinkedList<Integer>[] l;
	LinkedList<Integer>[] inversedl;
	public adjlist(ArrayList<String> g) {
		l = new LinkedList[g.size()];
		inversedl = new LinkedList[g.size()];
		for(int i=0;i<g.size();i++) {
			l[i] = new LinkedList<Integer>();
			inversedl[i] = new LinkedList<Integer>();
		}
		for(int i=0;i<g.size();i++) {
			String[] line_arr = g.get(i).split(" ");
			int number = Integer.parseInt(line_arr[0]);
			for(int j=0;j<number;j++) {
				l[i].add(Integer.parseInt(line_arr[j+1])-1);
				inversedl[(Integer.parseInt(line_arr[j+1])-1)].add(i);
			}
		}
	}
	public void getSCC() {
		
	}
	public void DFS() {
		
	}
}
