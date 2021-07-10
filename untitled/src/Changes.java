/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * @author USER
 */

import java.util.Scanner;

import static java.lang.System.*;

public class Changes {

    public static void main(String[] args) {

        //Declare scanner class since require user input
        Scanner input = new Scanner(System.in);

        //Declaring variable "digits"
        int num1;
        int num2;
        int num3;
        int num4;
        int digits;

        //For user input
        out.println("Enter 4 digits integer to be encrypted: ");
        //Storing user input
        int number = input.nextInt();

        num4 = number % 10;
        number /=10;
        num3 = number % 10;
        number /=10;
        num2 = number % 10;
        number /=10;
        num1 = number % 10;

        //Encryption
        num1 = (num1 + 7) %10;
        num2 = (num2 + 7) %10;
        num3 = (num3 + 7) %10;
        num4 = (num4 + 7) %10;

        //change to string
        String a=String.valueOf(num1);
        String b=String.valueOf(num2);
        String c=String.valueOf(num3);
        String d=String.valueOf(num4);

        //swap 1st to 3rd, 2nd with 4th. so we print out encrypted int as cdab

        //Encryption begins
        out.println("The digit you are encrypting is " + c + d + a + b + ".");


        //For user input
        out.println("Enter 4 digits integer to be encrypted: ");
        //Storing user input
        number = 0;
        number = input.nextInt();

        num4 = number % 10;
        number /=10;
        num3 = number % 10;
        number /=10;
        num2 = number % 10;
        number /=10;
        num1 = number % 10;


        //Decryption
        num1 = (num1 + 3) %10;
        num2 = (num2 + 3) %10;
        num3 = (num3 + 3) %10;
        num4 = (num4 + 3) %10;

        //swap 1st to 3rd, 2nd with 4th. so we print out encrypted int as cdab

        //change to string
        String a2=String.valueOf(num1);
        String b2=String.valueOf(num2);
        String c2=String.valueOf(num3);
        String d2=String.valueOf(num4);

        //swap 1st to 3rd, 2nd with 4th. so we print out encrypted int as cdab

        //Encryption begins
        out.println("The digit you are encrypting is " + c2 + d2 + a2 + b2 + ".");
    }
}
