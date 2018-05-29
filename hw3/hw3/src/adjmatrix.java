import java.util.ArrayList;
import java.util.Stack;
import java.util.Collections;

public class adjmatrix {
	int [][] m;
	int [][] inversedm;
	public adjmatrix(ArrayList<String> g) {
		m = new int[g.size()][g.size()];
		inversedm = new int[g.size()][g.size()];
		for(int i=0;i<g.size();i++) {
			for(int j=0;j<g.size();j++) {
				m[i][j] = 0;
				inversedm[i][j] = 0;
			}
		}
		for(int i=0;i<g.size();i++) {
			String[] line_arr = g.get(i).split(" ");
			int number = Integer.parseInt(line_arr[0]);
			for(int j=0;j<number;j++) {
				m[i][Integer.parseInt(line_arr[j+1])-1] = 1;
				inversedm[Integer.parseInt(line_arr[j+1])-1][i] = 1;
			}
		}
	}
	public void getSCC() {
		Stack<Integer> finished = new Stack<Integer>();
		boolean[] visited = new boolean[this.m[0].length];
		for(int i=0;i<visited.length;i++) {
			visited[i] = false;
		}
		DFS(0, finished, visited);
		for(int i=0;i<visited.length;i++) {
			visited[i] = false;
		}
		
		ArrayList<ArrayList<Integer>> scc = new ArrayList<ArrayList<Integer>>();
		IDFS(scc, finished, visited);
		
		ArrayList<Integer>[] result = new ArrayList[this.m[0].length];
		for(int i=0;i<scc.size();i++) {
			Collections.sort(scc.get(i));
			result[scc.get(i).get(0)] = scc.get(i);
		}
		for(int i=0;i<result.length;i++) {
			if(result[i] != null) {
				for(int j=0;j<result[i].size();j++) {
					System.out.print(result[i].get(j)+1 + " ");
				}
				System.out.println("");
			}
		}
	}
	public void DFS(int init, Stack<Integer> finished, boolean[] visited) {
		Stack<Integer> now = new Stack<Integer>();
		now.push(init);
		visited[init] = true;
		while(!now.isEmpty()) {
			int i=0;
			for(i=0;i<this.m[now.peek()].length;i++) {
				if(this.m[now.peek()][i] == 1 && visited[i] == false) {
					break;
				}
			}
			if(i == this.m[now.peek()].length) {
				finished.push(now.pop());
			}
			else {
				now.push(i);
				visited[i] = true;
			}
		}
		for(int i=0;i<visited.length;i++) {
			if(visited[i] == false) {
				DFS(i, finished, visited);
				return;
			}
		}
	}
	public void IDFS(ArrayList<ArrayList<Integer>> scc, Stack<Integer> finished, boolean[] visited) {
		Stack<Integer> now = new Stack<Integer>();
		ArrayList<Integer> result = new ArrayList<Integer>();
		now.push(finished.peek());
		visited[finished.peek()] = true;
		while(!now.isEmpty()) {
			int i=0;
			for(i=0;i<this.inversedm[now.peek()].length;i++) {
				if(this.inversedm[now.peek()][i] == 1 && visited[i] == false) {
					break;
				}
			}
			if(i == this.inversedm[now.peek()].length) {
				result.add(now.pop());
			}
			else {
				now.push(i);
				visited[i] = true;
			}
		}
		scc.add(result);
		while(!finished.isEmpty()) {
			if(visited[finished.peek()]) {
				finished.pop();
			}
			else {
				break;
			}
		}
		if(finished.isEmpty())
			return;
		else
			IDFS(scc, finished, visited);
	}
}
