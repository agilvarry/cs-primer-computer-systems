"""
Plan
-parse pcap header
obj: confirm version #

Parse:

- per-packet header
- link layer header (loopback 4 bytes)
- ip header (at least the length, can be variable)
- tcp header (syn/ack flags, ports)
gotchas:  
- little endian, network protocols use big endian 
   
"""   
   
if __name__ == "__main__":  
    # parse ipv4 header
    # get header length
  

    with open('synflood.pcap', 'rb') as file:
        import struct
        pcap_header = file.read(24)
        
        magic_number, major_version, minor_version, Reserved1, Reserved2, snapshot, ll_header_type = struct.unpack('<IHHIIII', pcap_header)
        assert magic_number == 0xa1b2c3d4
        assert major_version == 2
        assert minor_version == 4
        assert ll_header_type == 0
      
        while True:
            packet_header = file.read(16)    
            if len(packet_header) == 0:
                break
            timestamp, microseconds, captured_length, untruncated_length = struct.unpack('<IIII', packet_header)
            assert captured_length == untruncated_length
            llh = file.read(4)
            assert int.from_bytes(llh, 'little') == 2
            packet_data = file.read(captured_length-4)

            version_ihl, dscp_ecn, total_len, id, flags_fragoff, time_protocol, head_check, sa, da = struct.unpack('>BBHHHHHII', packet_data[:20])
            ihl = (version_ihl & 0x0f) << 2
            assert ihl == 20
            tcp = packet_data[20:34]
            sp, dp, _, _, flags = struct.unpack('!HHIIH', tcp)
            data = packet_data[40:]
            syn = (flags & 0x0002) > 0
            ack = (flags & 0x0010) > 0
            print(sp, dp, syn, ack)

            # break
           