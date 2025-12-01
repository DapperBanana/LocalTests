using System;
using System.IdentityModel.Tokens.Jwt;

public class JwtValidator
{
    public static bool IsJwt(string token)
    {
        var handler = new JwtSecurityTokenHandler();
        try
        {
            // Validate the token without checking the signature
            var jsonToken = handler.ReadJwtToken(token);
            // Additional checks can be added here if needed
            return true;
        }
        catch (ArgumentException)
        {
            // Token is null or whitespace
            return false;
        }
        catch (FormatException)
        {
            // Token is not in a valid JWT format
            return false;
        }
        catch (InvalidOperationException)
        {
            // Token parsing failed
            return false;
        }
    }
}