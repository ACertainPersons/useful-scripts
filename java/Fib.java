import java.util.Scanner;
import java.lang.Math;

public class Fib{
	static double math(double entry){

	double phi = (1+ Math.sqrt(5))/2;
	double psi = (1- Math.sqrt(5))/2;

	double end = (Math.pow(phi, entry) - Math.pow(psi, entry))/(Math.sqrt(5));

	return end;
	}

	public static void main(String[] args){

	double entry;
	double solution;
	int times = 0;

	Scanner input = new Scanner(System.in);
	System.out.print("Enter the n: ");
	entry = input.nextDouble();
	input.close();
	
	while (times < (entry-1)){
		times += 1;
		solution=(int)math(times);
		System.out.println(solution);
	}

	times+=1;
	solution=(int)math(times);
	System.out.println("Solution:" + solution);
	}
}
