using System;
using System.Net;

public class IPv6Validator
{
    public static bool IsValidIPv6(string address)
    {
        if (string.IsNullOrEmpty(address))
            return false;

        IPAddress ipAddress;
        return IPAddress.TryParse(address, out ipAddress) && ipAddress.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6;
    }
}