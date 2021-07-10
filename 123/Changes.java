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
        num1 = input.nextInt();
        num2 = input.nextInt();
        num3 = input.nextInt();
        num4 = input.nextInt();

        //Encryption
        num1 = num1 + 7;
        num2 = num2 + 7;
        num3 = num3 + 7;
        num4 = num4 + 7;

        //Encryption begins
        out.println("The digit you are encrypting is " + num1 + num2 + num3 + num4 + ".");


        //Takes the first four number from digits and store it in the variable "


    }
}
