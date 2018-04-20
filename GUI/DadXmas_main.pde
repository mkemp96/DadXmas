import processing.serial.*;
import processing.net.*;

Client client;
MyIPData netData;

// Used to indicate a new message
float newMessageColor = 0;
// A String to hold whatever the server says
String messageFromServer = "";
String serverMessage = "No message sent yet!";
int CLIENTID = 24;

String val;

import g4p_controls.*;



Table mainTable;
int rectX, rectY, rectSize;
boolean rectOver = false;
color rectColor, rectHighlight;
boolean driverPresent;
boolean Activated;
int gateBreak;
boolean primed;

String saveName1, saveCar1, saveLap1;
float displayTime, oldMillis, currentMillis, startMillis, pingMillis1,pingMillis2;

void settings(){
  size(640, 360);
}

void setup(){
  createGUI(); 
  window1.close();

  primed = false;
  gateBreak = 0;
  displayTime = 0;

  oldMillis= millis();
 
 //customGUI();
 
  mainTable = new Table();
  mainTable.addColumn("Name");
  mainTable.addColumn("Car");
  mainTable.addColumn("Lap No.");
  mainTable.addColumn("Time");
 
  TableRow newRow = mainTable.addRow();
  newRow.setString("Name", "John example");
  newRow.setString("Car", "Ford Ka example");
  newRow.setString("Lap No.", "1 example");
  newRow.setFloat("Time", 54.31);
 
  saveName1 = "";
  saveCar1 = "";
  saveLap1 = "";
 
  driverPresent = false;
   
  saveTable(mainTable, "TrackTimes/"+day()+"-"+month()+"-"+year()+"-AutoTest.csv");
  
  //printArray(Serial.list());

    
  netData = new MyIPData();
   
  client = new Client(this, "192.168.1.1", 7777);
  println("Client: " + client.active());

  pingMillis1 = millis();
}





void draw(){
  
  if(client.available()>0){
    
    if(primed){
  // RecordTime();
    }
  }
  
 if(Activated){
  
  if(millis()>pingMillis1 + 5000){
    
    pingMillis1=millis();
    if(pingPi()){
      
      
       fill(0,250,0);
       primed = true;
    }
  
  else if(client.available()<1){
    
    
     fill(250,0,0);
  primed = false;
  }
  }
 
  
 }
 if(!Activated){
   
   primed = false;
   fill(250,0,0);
  ellipse(550,50,50,50);
  
 }
  update(mouseX,mouseY);


 
   
   if(gateBreak ==1 && primed){
     
   
     currentMillis = millis() - startMillis;
     displayTime = currentMillis/1000;
     StoredTime.setText(Float.toString(displayTime));
     println(displayTime);
     println(gateBreak);
   }

}


void update(int x, int y) {
  


}





void mouseClicked(){

}
  
 

public void newDriver(String Name, String Car, String Lap){
  
  saveName1 = Name;
  saveCar1 = Car;
  saveLap1 = Lap;
  
  StoredName.setText(saveName1);
  StoredCar.setText(saveCar1);
  StoredLap.setText(saveLap1);
  StoredTime.setText("Time...");
 
 driverPresent = true;
 
 
}

public void clearNewDriver(){
  
  if(gateBreak != 1){
    
   StoredName.setText("");
  StoredCar.setText("");
  StoredLap.setText("");
  StoredTime.setText("Time...");
  
  driverPresent = false;
  }
}

public void addDriverToTable(String finishedName,String finishedCar,String finishedLap, float finishedTime){
  
 TableRow newRow = mainTable.addRow();
 newRow.setString("Name", finishedName);
newRow.setString("Car",finishedCar);
newRow.setString("Lap No.", finishedLap);
newRow.setString("Time",(Float.toString(finishedTime)));
  
  saveTable(mainTable, "TrackTimes/"+day()+"-"+month()+"-"+year()+"-AutoTest.csv");
  
}

public boolean pingPi(){
 client.write("pr");
 println("sending: 1");
 boolean connected = false;
 
 if (client.available() > 0) { 
    // Read it as a String
   messageFromServer = client.readString();
   println(messageFromServer);
   println("Connected");
   
   fill(0,250,0);
  ellipse(550,50,50,50);
    // Set brightness to 0
    newMessageColor = 0;
    
    connected = true;
  }

return connected;
  
  
  
}

public void RecordTime(){
  
 if(gateBreak == 0){
   
   startMillis = millis();
   displayTime = 0;
   gateBreak = 1;
   
   StoredTime.setText("0");

 }
 
 else if(gateBreak == 1){
   
   gateBreak = 0;
   
   saveDetails();
   

  
 }
  
}

public void saveDetails(){
  
  
   StoredTime.setText(Float.toString(displayTime));
   LastDriver.setText(saveName1);
   LastDriver.setTextPlain();
   LastCar.setText(saveCar1);
    LastCar.setTextPlain();
   LastLap.setText(saveLap1);
   LastLap.setTextPlain();
   LastTime.setText(Float.toString(displayTime));
    LastTime.setTextPlain();
  
  addDriverToTable(saveName1,saveCar1,saveLap1,displayTime);
  
}


public void buildNewDriver(){
  
  
   window1 = GWindow.getWindow(this, "Window title", 500, 500, 400, 150, JAVA2D);
  window1.noLoop();
  window1.setActionOnClose(G4P.CLOSE_WINDOW);
  window1.addDrawHandler(this, "win_draw1");
  DialogueTitle = new GLabel(window1, 117, 16, 150, 50);
  DialogueTitle.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  DialogueTitle.setText("Enter Driver Details");
  DialogueTitle.setTextBold();
  DialogueTitle.setOpaque(false);
  NameInput = new GTextField(window1, 13, 78, 81, 30, G4P.SCROLLBARS_NONE);
  NameInput.setPromptText("Enter Name");
  NameInput.setOpaque(true);
  NameInput.addEventHandler(this, "NameInput_Change");
  CarInput = new GTextField(window1, 101, 77, 85, 30, G4P.SCROLLBARS_NONE);
  CarInput.setPromptText("Enter Car");
  CarInput.setOpaque(true);
  CarInput.addEventHandler(this, "textfield5_change1");
  LapInput = new GTextField(window1, 196, 77, 85, 30, G4P.SCROLLBARS_NONE);
  LapInput.setPromptText("Enter Lap No.");
  LapInput.setOpaque(true);
  LapInput.addEventHandler(this, "textfield5_change2");
  Add_Driver = new GButton(window1, 300, 77, 80, 30);
  Add_Driver.setText("Add Driver");
  Add_Driver.setLocalColorScheme(GCScheme.GREEN_SCHEME);
  Add_Driver.addEventHandler(this, "Add_Driver_Details");
  Cancel = new GButton(window1, 301, 115, 69, 26);
  Cancel.setText("Cancel");
  Cancel.setLocalColorScheme(GCScheme.RED_SCHEME);
  Cancel.addEventHandler(this, "Cancel_Driver_Details");
  window1.loop();
  
}
