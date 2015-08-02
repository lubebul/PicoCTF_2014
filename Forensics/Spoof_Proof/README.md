# Spoof Proof
使用Wireshark打開[traffic.pcap](traffic.pcap)，發現有幾個人把IP位址隱藏起來，但MAC實體位址是不會改變的。
 * 看到最後下載secretfile.txt的
  * 得到其中一個他使用的IP位址：192.168.50.4
  * MAC實體位址：08:00:27:2b:f7:02
 * 再使用這個MAC位址，往前收集資訊，發現
   * 他上某社交網路的名字是：john.johnson
   * 得到他使用的另一個IP 位址：192.168.50.3
