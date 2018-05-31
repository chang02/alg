import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Stack;
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
		Stack<Integer> finished = new Stack<Integer>();
		boolean[] visited = new boolean[this.l.length];
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
		
		ArrayList<Integer>[] result = new ArrayList[this.l.length];
		for(int i=0;i<scc.size();i++) {
			Collections.sort(scc.get(i));
			result[scc.get(i).get(0)] = scc.get(i);
		}
		System.out.println("adjacency list result");
		for(int i=0;i<result.length;i++) {
			if(result[i] != null) {
				for(int j=0;j<result[i].size();j++) {
					System.out.print(result[i].get(j)+1 + " ");
				}
				System.out.println("");
			}
		}
		System.out.println("adjacency list executing time: " + (end1-start1)+(end2-start2));
		System.out.println("");
	}
	public void DFS(int init, Stack<Integer> finished, boolean[] visited) {
		Stack<Integer> now = new Stack<Integer>();
		now.push(init);
		visited[init] = true;
		while(!now.isEmpty()) {
			int i=0;
			for(i=0;i<this.l[now.peek()].size();i++) {
				if(visited[this.l[now.peek()].get(i)] == false) {
					break;
				}
			}
			if(i==this.l[now.peek()].size()) {
				finished.push(now.pop());
			}
			else {
				int temp = this.l[now.peek()].get(i);
				now.push(temp);
				visited[temp] = true;
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
			for(i=0;i<this.inversedl[now.peek()].size();i++) {
				if(visited[this.inversedl[now.peek()].get(i)] == false) {
					break;
				}
			}
			if(i == this.inversedl[now.peek()].size()) {
				result.add(now.pop());
			}
			else {
				int temp = this.inversedl[now.peek()].get(i);
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
