//
// A class to get your computers IP address.
//

import java.net.InetAddress;


class MyIPData {

  String address ;
  String name ;


  MyIPData() {
    address = getIPAddress() ;
    name = getIPName() ;
  }

  String getIPAddress() {

    InetAddress inet;
    String HostAddress = new String();

    try {  
      inet = InetAddress.getLocalHost();
      byte[] ipAddr = inet.getAddress();
      String raw_addr = inet.toString();
      String[] list = split(raw_addr, '/');
      HostAddress = list[1];
    }
    catch (Exception e) {
      println( "Can't get IP address" ) ;
    }
     
    return HostAddress ;
  }

  String getIPName() {

    InetAddress inet;
    String HostName= new String();

    try {  
      inet = InetAddress.getLocalHost();
      HostName = inet.getHostName();
    }
    catch (Exception e) {
      println( "Can't get IP name" ) ;
    }

    return HostName ;
  }
}
