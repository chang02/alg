import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class adjarray {
	int[][] a;
	int[][] inverseda;
	int size;
	public adjarray(ArrayList<String> g) {
		a = new int[g.size()+1][g.size()+1];
		inverseda = new int[g.size()+1][g.size()+1];
		size = g.size();
		for(int i=0;i<=g.size();i++) {
			for(int j=0;j<=g.size();j++) {
				a[i][j] = 0;
				inverseda[i][j] = 0;
			}
		}
		for(int i=0;i<g.size();i++) {
			String[] line_arr = g.get(i).split(" ");
			int number = Integer.parseInt(line_arr[0]);
			for(int j=0;j<number;j++) {
				a[i+1][a[i+1][0]+1] = Integer.parseInt(line_arr[j+1]);
				a[i+1][0]++;
				inverseda[Integer.parseInt(line_arr[j+1])][inverseda[Integer.parseInt(line_arr[j+1])][0]+1] = i+1;
				inverseda[Integer.parseInt(line_arr[j+1])][0]++;
			}
		}
	}
	public void getSCC() {
		Stack<Integer> finished = new Stack<Integer>();
		boolean[] visited = new boolean[this.size+1];
		for(int i=0;i<visited.length;i++) {
			visited[i] = false;
		}
		long start1 = System.currentTimeMillis();
		DFS(0, finished, visited);
		long end1 = System.currentTimeMillis();
		for(int i=0;i<visited.length;i++) {
			visited[i] = false;
		}
		
		ArrayList<ArrayList<Integer>> scc = new ArrayList<ArrayList<Integer>>();
		long start2 = System.currentTimeMillis();
		IDFS(scc, finished, visited);
		long end2 = System.currentTimeMillis();
		
		ArrayList<Integer>[] result = new ArrayList[this.size+1];
		for(int i=0;i<scc.size();i++) {
			Collections.sort(scc.get(i));
			result[scc.get(i).get(0)] = scc.get(i);
		}
		System.out.println("adjacency array result");
		for(int i=1;i<result.length;i++) {
			if(result[i] != null) {
				for(int j=0;j<result[i].size();j++) {
					System.out.print(result[i].get(j) + " ");
				}
				System.out.println("");
			}
		}
		System.out.println("adjacency array executing time : " + (end1-start1)+(end2-start2));
	}
	public void DFS(int init, Stack<Integer> finished, boolean[] visited) {
		Stack<Integer> now = new Stack<Integer>();
		now.push(init);
		visited[init] = true;
		while(!now.isEmpty()) {
			int i;
			boolean find = false;
			for(i=1;i<=this.size;i++) {
				if(this.a[now.peek()][i] != 0 && visited[this.a[now.peek()][i]] == false) {
					find = true;
					break;
				}
			}
			if(find == false) {
				finished.push(now.pop());
			}
			else {
				int temp = this.a[now.peek()][i];
				now.push(temp);
				visited[temp] = true;
			}
		}
		for(int i=1;i<visited.length;i++) {
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
			int i;
			boolean find = false;
			for(i=1;i<=this.size;i++) {
				if(this.inverseda[now.peek()][i] != 0 && visited[this.inverseda[now.peek()][i]] == false) {
					find = true;
					break;
				}
			}
			if(find == false) {
				result.add(now.pop());
			}
			else {
				int temp = this.inverseda[now.peek()][i];
				now.push(temp);
				visited[temp] = true;
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
