import base64
import urllib
import requests

API_KEY = "Vp4CabaD4MIpYGzs5FMMWSHY"
SECRET_KEY = "bcQqlhicNFTZkByO7lsw59sj9hDYSwvf"

def main():
        
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice?access_token=" + get_access_token()
    
    # ofd_file 可以通过 get_file_content_as_base64("C:\fakepath\031001900511_84911760.ofd",True) 方法获取
    payload='ofd_file=UEsDBBQAAAAIAHmmeFFSgvYrMgIAAGcFAAAHAAAAT0ZELnhtbJ2UXWsTQRSG7%2FMrhrnP7sxmd7MTkilpl4hKFZIoeCWbZJoEsjthP5r2rt5oLsRaKHpTsVUKRbEKFiTRn5PPf%2BEkm2RTS5HtzS7nnfM%2Bc%2Bbszslu7NktsMtcr8mdHMQSgoA5VV5rOvUcfFIuJA24QRNZvlPLPC6YQGQ7XkZEOdjw%2FXZGljudjiRir82qEnfrsoKwDoHJq%2BX9NstBYYLgacTHkCYAmPNEziav7c%2FiSLnv7PBQWdNMaikEVzBLY6QYapWkLUXV01aKaRXCdIwrWTnKXXfnA7%2FBXbrVaDoWKFt7Yd5CXU%2FccpnlixpNy2dUQQpKYpxU1DD%2F2uI1V%2BD53Bay5S31GyvgkWWLRvjMbreEP7loNqSi2ZKCJKQqymKbled%2FMEeUs8uSbZfXgipzIS0FHdZqFbhrl8yHcWlLzM3SdJSKCxseHo3PLwa%2FP49PX0CKUhghTBDSML4baXj4a04yVIJxWkexKW%2B7k8uz8cWb6acPkCqzU92RMX11tGSgO1H%2BHIjzjN6fj04%2Bwvk%2FNuxdYTw66SqqUOPiRqdn0y%2Bvwy4bRCNAF13WARYdJ4AYuha7wMnVt0Hvx%2Bhdb9z%2FKRo26Pcn318Ou1%2FFJ4CUYE1cbZTazusPSPFZihhx8dPjg%2BHx5a14UTdG6nYeF4rmpqbfuw3%2Fr764edEEWE2Q5fwocu5T8X6OZPEMbOb4khhkK8d8PXKUmnVxvwKXeQvTTPDkSI7Ma6mJtRLCsRaGYgDSxF9QSwMEFAAAAAgAeaZ4USqKDfbEAwAA0woAACAAAABEb2NfMC9TaWducy9TaWduXzAvU2lnbmF0dXJlLnhtbLWWWY%2BqShDH3%2BdTEF7NZVNUJqMnsrmvIIIvE5YGUWgQGhA%2F%2FcXRWc7k5Hpu4ryU3WVX8et%2FQXe9%2FDqFAZaDJPUj2MFpgsIxAO3I8aHXwdeq%2FE8b%2F9V9eolc51nxPWiiLAFYFQPT58rXwXcIxc8kWRQFUc3TGNhElHgkQ9FNvPuEYR%2BRwBlCN7q4bs5FEuW%2BAxLsfTAzQ9DBvSg0ffgKUmAGOKa9kzEXMiEKYxOW74tw8ku6D7opQLvI6dIEQ9Bsk6ApmmsRNMFS9Av5p4V%2FSCGaCKh%2BCLoMVW2EZho0w9IsRTSa1PZbko%2Bln2lWwAVJJSJIMWEH7MP1ORdxfydqUDR%2BDfseiMl%2BAKpZByfFyH6lyB6EEUrJhemB95mJKl2IqhIfOW5Z3p6pmUEGuqZbcJNlMChJX44N7yjrTMprG2kSB3HNHGa1zOGjolDPaNi57utL8DsZ%2BRvaXwIvMivw7RVI7xDSPWSktYIXJ9mULstVfd44c5LKs2c55%2BJUXaydrQbteh2mDyasbBYCiO4zNvTppmdbRnMFN%2FwQ9HhpbBuwBXzuWB%2FHmlJ6I5%2FtiaowPTxaxareH1UXIogq3juwqQ63hdGEy%2FUkMQzYyGrwpOlobrTy9TQrFNpTmnPSKv3UeDCsGgfpxfw1qigxe13I1dYylybWLFKALqBcb7meXexrVgITMa6Lw1nWNn6o9ncA57SoUIJr8nRrMupxxzHFNufBaib5DeS5tj7fjTgQuAsfSI%2FW0vRSUshSFIWX4R3OttU%2BHxzOmtWizabk%2Br7WWDl6K%2BLLpb1eNGZrTmf4oySSq%2BmPct7BREHLq055trYdaAfaXHoer%2BdoYhrltG7zQdCG8bbphFuWfvRp1EPItHfp7fdS%2BXuSLkAysYytbG1Uv9zTZMlZVMudzHpyXo76Ep9lR83dqHJr%2FOh3szqPSD%2B8fPJtithbzH9A2oZED%2FcFVOIps05OvOkrTaMNsvXRQFa%2BDZWkHW1mKxZQxQ8JGiW%2B50MzePVhHvk2uKOqQEGgFW5NYPtocHaXgqXMgXxeOIWMPC07jnriCHhzyc%2BoRwNfL9DPm%2FPeC5CdwLzJntQBFHh1PEn7mhJN5zQdSk0dCkF93M%2BWg%2FAgb86PQ53L4h0qlewfU5jDwQ7Im%2FVpsbP5CaOslWE9tCBvnqnpOD%2BEaGDs%2F%2BeX%2Fs2Zfu2KkBnGb8JhQ7HqYnDsciG9EVdjPsqgYyZVT8ZRBEVh7Yupvw2Zi732aJ9N02cb%2BKUzvPLdSnVxpW%2F2Nrn9Tzgm%2Bprntqlv%2FVj36V9QSwMEFAAAAAgAeaZ4UV6aZX1fDgAAbRgAACIAAABEb2NfMC9TaWducy9TaWduXzAvU2lnbmVkVmFsdWUuZGF07Zh5PFT7%2B8BnOWbIIIwhu8q%2BnRlLiGyRbRhC1sLQILshV6UMTdkpUUrZU7K02BKyNF3VpU1FN7oxTZErW5p0%2BR3Rort87%2B%2F3ur%2FvX%2Fczrzmf8zznOc9zns%2F5LOf9AWkiASBNsBABB6DKFKTxFoJ8OITZVkiBQ22xIxpb2uJ4NfAgHtQElwoepAH3EXAkZj3zZDOzqo5Vns5MLnx5oIl58cBwQ%2FLL2npmA21JCWkQcDhkHwrQgF1QTYH%2BqwqQCDgCgRZAwmAw%2FrMgBsWpFC%2Fe4wRPiOKAgS54bpALhXQCUIIIU1u8GLhmUeDGCPw%2BGF4FVFq8iMSsW1KzsmuZlZmvquOHG8tYVYWsTPpwQyWzNUFhK5GgCEoK8%2BB1oUS0ltJwE%2BYhEPAEKLUlEdy1MrIqqLwU%2BW%2Bl%2Bdn8b7YK6AoKotBKdItuAwT8c%2F40VaQJDNibMqo%2FGVSwN%2BZHWnWwSsKz9dwpZvEMRGZecE2gDQGOeOrBnTY7HCW5D3uat0zen1INrxNRMJ7XPofuHjT8ocm5mIYoB2mIEpAXeh4JPjh8AQCQCOR7qJ0hWXBRRoAwUGpRWgeIgLgD2IaaPC%2F0CEd9TT3rtkk0XjFXKPoyKLFowAvgAKyOfHbM0%2BcVdfa1QJ6s0jwrTsTJGNyM4oIenz7LA%2BfiAzaAWlA4ziUFEoFAwA58IwOfZDSKQ5kXiUCDq75cQIPx84tRpID4d2D8FLi3ILYghh7tT6WG6amrU71jArzVIv29Qyj%2B3gFqZP%2BAEG9Ip0YJjVYjh%2BgRNHR01ckhBuSIIDwB1FAJjVo6XT5RIRuQQwzJfhHUgJ0BZG%2Bqn4NfdChUB4SG2AREUlWUDH28I%2F0MvzoAIwvCC0LpwUG%2B3l%2Bj%2F78HtUBxKqPgHBxoOBzQB%2FVAnc8yCKer%2FL2GwGtr6eiog%2BtQq6A7Afg5U18OTkAIIwhqqH4arTvxeIKWLgGvpamxwojrz4wEvhpBswCAQWjhod7AoeTMjUYAWIzAH3Rn3NJlJMCD4cZ%2FHlJQkURxetEt4PT3plyAAGY1FAiE0l6eRzQ0V459pCUMNEfIwCozpwZ05%2B%2B%2FFTewCtTPOS4VGMRyHvUVY1xpNbyDOxAXCJmMFUn%2BhO%2Bkhiada6K8yyJaHeDqTEzUlbhkUf7T%2FMHisnYRPgK4YrB%2FUWjitb8oCBqgFkFnWQHSuNJxyNCdvgCNaz%2FJGglgoemJE1aScpQ0Qt2zbQSSCuEwmABUbw4l7wDVoWNUsF8IVS0mOMgv82lgB4ihj09hzWdT8sFozqTb%2FaBCEMiI9dR%2FbM2T5OSz23KwxTby1et2xofShcsl1EfOsuxttb3%2BhMMmqM1rksSCkzHOhuN86uCQcfL%2Bk%2Bu3NFZnh3e6pxKvZbc9avQ0CXigWZgxZtu1epTGUIlFSK6OIKjVnL873J5kK9ppd68qNfr2qZsZis3O3U47ikihtaKpxQ0GLqpmujdzNNotxNlTH37eqnbU4NBAQuyd%2BfqHk%2B6um5ofqUx38KQrSqRmjhqXocaIHb4n5pwQJ7grNpF2hikVPWveSY1nsFWjpeAGl9EkqdSKl238K1tGrFP5YzskSUItI%2FSlZUhRPkEBZAe%2FyB3gYuM4pdvzthmtpg%2Fm%2BxDGr3KuTesFZAT4FXnvPiyXu3r5dUh2pE6CRkyEWDjv01hS6MIsZV5dA6PWx9WdfTL7WGfdYxNpoalNTkmdz6IfiXuBgRh2zawp4XnVsQkJS323in0yyUVvxcWIF2%2F%2BsFavMlrKW3yNW4TKvbSwh7ByjIbzo2xHsouNbDT%2FrWvJhCPvWwy394glB8rNR%2FcGtst3b9BLPvfrh9pjFw%2FVNAdSuFnkWdvAn%2FImuSh5QorK4aTZhTWtTi4MvpVJ6%2FaQpZQ5YDBuHJT416S9KX6Rn46QYBoaQl3uGjeOE3eJbRG5Oc7Gdgxo5FEGbrrwZqUVZpISnmkb3Hr3yLnCytzZp%2BksSSFb3C22u3CscLUCNtZflPM37aiPWh%2FO9PW23CBK5wTnm%2Fe86b4zdZIVtW08P85gp91k34S%2F3mtKpxljsmuAul9T9xXlzJuggZm%2B5tqNFQ%2FU322ro6N1O4aODgl9HKMcmmLfs6reHRHRPrHwXmFw6EGfsd2qS339Eoz71rMUNjivuBAicVoi4x19qG2aSgTbsr0cLry7unVibPvUzPTkByqhR36KEcFHp7BT91251%2BPrfPh2Uv5H6vzEr7nsAf2fzqfylGXIz3X0uRpGerjjGsJTMcIDMcw1kk86R36zoQTtmSamc0w43u13HM1RDk1nDM28jtEjn%2BG9mTGUwDDiD7O%2BP1b8i2Si3GjUQIq825lfWW%2FsDZuUG1Y5NGZe7BmyNdEbItRlZbA6tth71UZ310R4uW5z4LtUO8VaOLUwMfniBh%2BrJ27f1PQM%2B4wdNzWFR1mtWfv47olLxO1H9vikCyqY2Y5u5Jtbg73O9vMicWSXOGOQpbIpGrZH1I57oHrvzhgdO2WhV2pd%2FshfCvF%2B7%2ByLESMPwcP0MpvIn00EDwsfETeTZuyaxK1PjYSvvZP1dgO04vl0ibgiwn1Lwrq8qng76w1WuSlV9eMEsgVqEvzfWLk0uBN4lGzMlPnRGzKA7cX5qlkipWnAkZTHhjskLP3Xynhc5RAsfmpzaqt0fGQm%2F8HgTF6lNq4Btk7DD3LDbYVvxV70uwjtrXs3XiELCAioKugxKrVXjwe3SyfmHpzzcmyw4zRmtKnC4k%2FkxJnqoF6s%2BfnlzTM51xPc9FX4gPX5FgJp60XphQcrXz1XEmwMl3yyI7DYSnST9J02cpy7iaNsXxF%2Fg%2BD7UtLajYWb%2B30FrLKI%2FGaxWXfkXok4hMQn2Q%2BoejCyBFbNeejvoCddSRZSbLxvoV12MshCZo7hQXY8EeVR4Lt%2B%2B%2FXQdlVprrA8whWB3LzU5JCp327LgvdU5fKK7xqZvdAT4lINas8%2BIZJ1rCjKi3d%2Br5iNCgeTezCpkOjKLSfcunAJkCvr6ow0S8XWnx%2FTKQvj40WalRCrtqaONC6Qi2pbJOXcikVdNm8b1reTKTtJsfby2aj7xMVctO5Jl%2B5VaSPbY3SH9JFGsUM0wesYYcUtawLumTWzR8dljQKEqhOpRwuO266lvzynKcjIzlkyXAtcc97meSR6E266usUTgR1Us2l4zJ88k2us6IqNuuXzNk7hsVM%2B52TUaHkp9gBtPpSL1C97wfSaFVvES%2B%2BZFJWPu9XS8qxoyQn3A2tLp6oSi8hyRlwp6e9HSL5NiTOHT3JgAfenPHUDXQTGed%2F1vQWnmnhAcyV3rRvtJS%2FmO1oEgnhYh4iESivZHGkajShUEX%2FZ7WFYeYj9xCYR4mSP%2BdyU6dvRwEaDM8TWW4PVZ%2BOse%2Baami5%2F7PLX6ZndQJ%2F6pd%2B0zKezYLWnrgSj2EZEs5S%2BcSy%2FxqZIY51xg9EaimyAFGUifVcyqpxw97Ru4cmeG8xrs2nMQHvyoJV%2FGBp1bFezS2SST48Vwf9UpcAjJcddnkW72F0XEkqjLs7wtEz5uDNx4X5Ffc91rNDKskfTralm9hOaJkZBnoQ383rVrv1PRGODT7C068yT3GQTyVbW99umMzVKTNX5TV0%2Fsodr3%2B54SKsNuq6S242ietaS1t8QrVAF0gyE16YZvZa1KXY7e6qQEXfM%2F66Oi%2ByFjB2q7%2BrypMLaDmruk69sPe8s5SA8Ln59YQG5cpodYj%2FkvAVJNtDagoZqO%2FPNS0utPTcNxB4c%2FE2IPK6rpSXoSXKYdtw8I7rrpNDDkFe3PsxWmitOX5rIz9%2FDu7vvVbhucdOFEcFy8bmqQ1mO4p2WEhHXXO32cEnayyc4lKQExKe6954rFJeqbSlL1CQOiVZVH2kiSVg8Z%2BPNn2rfu%2FnQ%2BNVREkwqIaal0enleaCCeoWG0k93aTe5OEuXydB5mmuvgsDJhT%2FhQ9mbu4XujnWwLCssulwatbcv%2Bkjr%2FVDmKqOtkeP6Pt1PzZTG8oL3C57ZfVbQe8NF%2Fxa6njrJGo7AIv%2F8M%2BNzqYuH%2FeFHx%2Ff3f78Yf71fFP4nS%2FP3Lr5f2r664EP8p4Xue1%2Ffv7%2BvvqLRX94myZoDtagEFn%2BQoR%2FnooSASyLgWBAHYlGrPn0fotAICCThMABJUMNDLGkOcaQJSEO%2BXGZJ%2BCJL4lr%2F6yyp%2FS1LfhVBv5WRZT7hFhRZhNkSD3ljHkllnc16mXyAmZHFvHiMWZKI1wDxS%2FGVfv9wS8%2FCTKthVRQwD9cNN59iXW5iNZ35C4oEui09f10Nvx%2BmZ4ZCt9%2BtkQsqxg0Fy5eYhU%2BXvdo%2Fd%2BhikyH66hU3rwSlQ3WYyR8c5c%2Ba%2FZg7XVImUaPbuv%2FCiRSIIpMhiqT%2FcxR5v5CSdFOjfF9QIEy080NVfQafYMw%2FRZEzyxQ5BsaPfOa4FfD0FxwHMclnjgPx%2FxeOW3Twv4XHfyao4TfwCPUfUP0beFz3l%2Fn%2FJ2YE8RAPEkAdDcKGP2fGb41%2Bx4x4XZD%2FMzNyYlBLHXkFJ4LflD%2FgRHCZIvEETcJ3nGgBA80Q0kbAUTmrMIKVZ3fitO9v3sKKV0m9WTzMoi5OrOuPChy1ECaO%2FkIbqs%2B9int%2BuP%2FHYMuJn3l5RWqCLHaMZjWZP%2Bhd55n51euyz7gOeb7UdGGBqffUC1al%2B%2Bq2ahadlosq099U4pwhenDmCuTzrvOdxDtX7aQweY6Dz7apJzX4D9noi9YLj5KPXoc9Ox%2F6CSyhpiFoQkQN8acbUgb2RM9FcyRd6APCIqo65wFbuXx4O7zktLuaubWHT2pQXD1ORn1pbt0aQAmJ%2FHRcFrypURF%2BixPlvxto%2F26g%2FbuB9u8G2n9pA%2B2bmXHZ6fncsg7%2FTHMe6RxXb7fM3mmxGK59HK4xxgax1cJymzjSIZOqDTWN2%2FceFzFSjzj6UIP%2FtlbB6MSb%2FdKaspj9j7c%2FCEj9H1BLAwQUAAAACAB5pnhRKhfapJwAAADbAAAAGgAAAERvY18wL1NpZ25zL1NpZ25hdHVyZXMueG1sVY5BC4JAEIXv%2Foph7u2ohwjZXSEkEOpUnUPWTYXaFdfSn9%2B6VOBl4D2%2BN3w8n58PeOvBddYITFiMoI2ydWcagdfLYbPDXEbc3uvs3DWmGl%2BDduBHxmW%2BFNiOY58RTdPEfHa9VswODaVxskUZAYTpqZqXdVnLlNO6%2BCH%2F71AWAlOEfeX00SqBVFh1i2kBXLjfEGjmVZC8Ia0VZfQBUEsDBBQAAAAIAJumeFFctEn32AAAADUBAAAiAAAARG9jXzAvQW5ub3RzL1BhZ2VfMC9Bbm5vdGF0aW9uLnhtbE3PUUvDMBQF4Pf9inDfTZq5iZYmQ5HBXsZg81liexcD7U1I09b9e6MbZU8598AHJ9Xmp2vZiLF3nhRIXgBDqn3jyCr4OG0fnmGjF5U%2FN%2BXBWHwl8ollQ32ZOwXfKYVSiGmaeL77gDX30YplIZ9A%2F7MrOV0CKjgm0wVgu3cFL4%2FAjsNXuvbOkklDxB1tXYtZHkw0HaY87C6zfX4VnAPfm%2BRG%2FGOgfXTWkWk%2FHY3e1ViJGei73N%2FmhIC5ohrZmx%2BoMfGiYMXXTBYrJuWaLQsQ2c3Tb3n%2BvV78AlBLAwQUAAAACACbpnhRFBopcPUAAADPAQAAEwAAAERvY18wL1B1YmxpY1Jlcy54bWxtkUFOwzAQRfc9hTX7xk0RUYniVGpQEQJVCMIBrHRaLCWeyDaEnoElZ2DLlhW3Ac6BKUFKGnb%2Bz35%2FZDuZP1Yle0BjFWkBYTABhrqgtdJbAbf5cjyDeTpKaLOOr9Eyf1rb2CcBd87VMedN0wQ%2B2xqLgMyWTydhBGwhLV5SIcBLkO71jEoyN7Us0B4Cdn4q4BhYvqvRK2cLX6CcvUKTUVWTRu0EzICnCf%2B3aUnadZb7uukJsJ%2BwkpXv%2FHp5%2B3h%2F9kRWqtz1GD8Qo7ArXkiVq773iwbaUVf7fH0azGvZQIy6Ykb3RqFhK2z6dnfj7yHae%2FP2d9LRN1BLAwQUAAAACACbpnhRaXrldPwAAADAAQAAFQAAAERvY18wL0RvY3VtZW50UmVzLnhtbI2QQU%2FCQBCF7%2FyKydxtS7WkadiSIClpAokR0CNZ2rGsbrvN7mL137uWRiNcPH5v35t9M9PZRy3hnbQRqmE49gIEagpViqZiuNtmNzHO0tFUvZTJIxlw7sYkjhgerW0T3%2B%2B6znNsWio8pSs%2FDMYThDk3tFIFQxfCtI8vNO8euOa1uWDIFwzvEFaioWdR2iPDwAujIZYJKe%2BVVBqeuDyR6xhNIA7hNkLo9U3LCydH6J8DG6vVG%2F074v%2FpcslD1%2FVJWrGmUvAroW8fu7NtP1s3M695RQiZ0jW3DJfzfBkOm%2FR2tw6l4tu0jwPv9RCeP%2Fx9G%2Fhn%2FpVgBsVdNh19AVBLAwQUAAAACACbpnhRfz8BZccGAABkGgAAHgAAAERvY18wL1BhZ2VzL1BhZ2VfMC9Db250ZW50LnhtbM1ZW28TRxR%2B768YrdQ%2BOMp47hdKjAiIqhURiNILfTPJNqQNMTKmQJ%2B4CCg0BaJShVQRCCiFqi0pbVLShPDQ3%2BJdO0%2F8hZ7ZXdvrzaV4caU68mbmzMXfucx3ztg7d505Pom%2B8KsnJypTQx7FxEP%2B1GhlbGJqfMj74PC%2BQePtKr2xs%2FLp2I6D5XEfwfSpkzugO%2BQdq9VO7CgWT58%2BjaF%2F8oQ%2FiivV8SIjVHmlaMVh%2F%2FiJyXLNR63Gu3uHPOahTw5Ux%2FzqkDdcHv18vFo5NTXmFeMVeypTNX%2BqFnf2l8%2F6VeTWKNLe8UztwNHP%2FNFaLIfNht36cvUs9CzSSDOksdLCemgfbAZS6qH3J770oYU1YSbZad%2FE5OSeymSlij4sT56CUSoVMgxx2cLiPmtPZcxHHw95YJYjQ57EWmrtob3%2BZK0M0nFECVJYMqu9Un35Wrj0LLh%2FJzj3vPH4euPWUvDrzXDuyfq574MbM42Hj3cW07uWOt1Yoc0VFGkFqRLwcQwJgmRbPd5Sj2OqpbcVdoGJgeE0dooolk5YIpwSQi0hktJcMGUaJleIE7Allkhi0ztQsRFosqS5uBQ8uxPOrYSXHgXnHzZXfgbTBk%2B%2FC%2Bevrs%2FdDC79EtxYzoVfZ%2FHLFn7exq9a%2BAVmnPNtFNDKTU4poBFsJrySpRKOB%2BEju9V79tARbk0utCaDllKGdR8NbmN7o3HEkxBpC1hWsGEGHIlWWCVHYvnC%2BuxS8950ML0Szi00z99qPlsQ3AY3nondIGNUB09%2BoEZRZShYh%2BSyid1gE41tP4OQdTS0GQ3DpR%2Fry%2FNxKK5%2F%2B6dT9cXN8OmV8NYCtK3hhBBtDBCjIe4lVB4VNclyAaXg9v6QgW6rZIQF26lcXtA0DZExxAQCXwjcM0IIaKb5FnSllLZEMa6V4blgdqUNymBnBofasVYfTMlabNV4cq9x83IwczsXRp4NaCL6Gc66zakvHqw%2FuBOzaePRTHjtXBzIL59%2FFUf3y%2BdXY35tLj6or67mZ1m9IZkx1rcAZqyTzYyVFinIZmA1yGwWWaNkvoCW3ZGiMEecIg2ETnpIDBwrS3WCXEnZjTzKDmhQaRwx7Ct0k%2BVHkuXEnTC0XROMQgqck7fGa29byowwRUoL0hQ45CM9oIrWjQwWpB6UalCSgbcma2%2FzoibEFgVVFgQwTriQA7TgxorGmkLBwgLhugXqnoIUSTxP22gHUWTCFMwAiYYlEdQOgoX0QC5fqMyJEATLbY4Ew0pIsw3D2Ay%2FxwuSJMcZs8jxYiJNJO05vDMntTIiqUg8aAg4XblxmcjSXuMW%2FNNeJp2H4uKmMX8eGuu3%2F4C0WV%2BZCX7%2FCVJkMD1bX%2FkF0ibTkDXXZ35ev7jWXLwfLEwHPzwKrv8ogqcXjDEw9vL5NDGSDkYPA%2FwoldS5rJ0tiSgxLXOLlLlfvSqSVOktqiLu8r4Y2U33Hdo7LNU7uQCbDelR961WFv9aB3XohxFGgr8WKQ3nv2IinH2YS5tsPSNUP9lfdYoZ2QYeB2BcwDQv3KuvrqXr6iQqv5kNb1%2BPCxvwGZAsFa6kYYzIV9Lz3eNwjUwpaqBk2HN4BM4jQe4v%2FpdW3oUdhzcjEeke8k9WTlVHo7ukIa3L2sFy7Vh6V5bsSrCQ0b6tRnpn6TjVamzgAIJ99k9M%2BR9NjNWOuWUtc%2B4%2BerTqfzEBl9exveVauTQCBwETDX6QAg0nHY5dcnYP6gaAG2AIhK5B41HaXhFPjEdhtUlWRM3hZJeoE%2B%2FdFiSfOQKnhkfv%2FTCmo3csc61Y5nqx%2BbPwY2nHWpsGn%2BmqPRRHFqIOWYjAXkNPxqG18W7hou23%2BvIV91y9655rv8Ez%2FPpFMH85%2FG4xz5kxmfoigsw12oSsOIZyXG0DmzEDd%2Fq%2Fc51dI18fB3iQOX06YLqK9WS4xOAFoZGrtjFd%2BZRy4XxM3WGDymEzqJs7Gi4hxhU0R9yUmEhymk33Bw%2FHrlLowMnccixxHM2As%2FLarTvRaJkTp8RK9cVutj94gAz1FnaTKbvltJolmavh%2F%2B%2FKZbtur1rkg4jlfwuyi%2BSkqwgUkiTPHRvIh6chJhVNGylqC8yGr3u8UqG5tlBf%2FbMQ3x%2FDuZXmxbX62rfh0teNP1Ybq3c%2FpDhfoGTYE%2BjPqUh7VFFhw%2BQ2anol%2BmYueF2sGZdkyt0eekIHJRnthlcKHs7mwpNhzTgiMNcEKibTGyoafd25icnS3w%2B9DnXaDHWq1wFrsNCbezgmrDbcvGC7eZXGju4VJXy62iIQO9eKxKp5UFLSRaw2YYSecaqNEfnvPwVEguhnmqTd%2Fv0mKTPH%2FdIb%2FwBQSwMEFAAAAAgAm6Z4URS%2BTWVTBQAAejcAABwAAABEb2NfMC9UcGxzL1RwbF8wL0NvbnRlbnQueG1s5ZtdT9tWGMfv%2BymOfL%2BDz%2FE5fkEk1QZCmsS0SnRbuTTEg2xpjIJb2l1RqQK28bJKtFM32GCjA%2B0FkNqtg2b7MsNJuOIr7Dl2ChwbJuZsyI5vArbs5Px%2F%2Bfs5%2F%2FPY6bt%2B73YF3XVqU2W3WlAIVhXkVMfcUrk6XlDeuzn4hqlcL17rcz8s9d6wxx0Eh1enemGzoEx43mRvT8%2F09DSG7alJZwy7tfEeqhJdKQZn9LtVz6l64caQfd%2BpoYGaPX3Drtm3CwpT0NsDBUVrH3zD9ibeHf3IGfOC3bqC3nLvVEt27T5smJgjYmATGRpSMZw5VK46H5RL3kRBUTHl7fcYLFcq%2FW7FraH37codBwRxHZkUaVxBwf7hSXsMdnOlJzxh2Ku5Hzv%2F6pQ3R0drzt2y7TmlAduzi%2B8gFYZE0VA4Nor6es47LNx7KvJc0UZctNn1os2zohlophZoBhulV3Q4uI5UW1HVnORANVGjsi2eB9kkKpuoWh5005humgvdmqxbQ5p4d4astGkGnSpoFn8t1pFkdlYyVXkuRPOzogk91UxpejXTzrwtJTNCrFyINuQvmuVCtBlzN1FZKFpNsWi1I9FW3N7dr5qqcX%2FnQLUUy7gOojkNNPMUX9S8o4uaSpHMpKeaWYqnadbRNE2lOGaxXGhmch3Lh2g5j2n5EC0HMj0fouVAZvCuFH3TueedFS0FMi5aZQwRHWkYLDDoVj04BOLLcPkTGJGGgcoVChdj7XdLDrolmMPMOgKjwYYG38aAU%2FHsW%2B0hodirUmysHvhPt5v1J%2F7yy%2BP6VyGM129YPN38BzaanGCYaJ4aouHQBXj85UfNZ9uHr75vrj9IiofE8RCti%2BiAczqgQ8%2BhY3aLe%2BozwKfx5bPG6rdJ%2BWhxPtkqPQybOoIX46TkrG8c%2FbjQgWWkfKVjQEGxCR9BiLhTRdNGRUSjkWAQvE1lRAxb40i8KMXWi18O9%2FcaT%2FYTwYjkLqQRAEI10SVJn0HE4i7uEALzqXAHC66ZLxabW3tJraFHaeii550pGhdUE7myNA%2BeN7eXDg8OWruz%2FvxPHUzeRoQYo6LxkCliDHOGxHgp5%2Bi0%2BK7u%2BWszf808aK782tpdS8rHjPIxsJExPpdyFMxVjfmXrY0Ff%2Fmz1osfOnCU3MajMC1QUaF5diu0vzsL05W%2FcJCEB5PiMQ1uOIN5LExgwZQ2Epc0kFI82thvfr0TFutEVKRUrGshFaJhA6hgnlkura2HjfW6%2F83ncAEl4iI3CQMqBtasjEGBa2bx8eEfi4kQyD1D8RiOsIaKRYzkGam5UDgg6T7eO5pbTsSARYqoQGCFBLIBgAsAwgSvkl0Hcq5lTLTfwQUkOwR0bECdnHt09N1aIgKR5qIeEjBw1gokpNXtpebSXCIIcjw127MnIaKjlxUKOraMAEJSJ0gZlFJkETABMSGDpjVAaJifWd9Rsaybb%2B1sJFIv50mxoLOCLogeRMqMeOASGfx1hICKCV4JgR3X5%2F3NLX%2F26XH90yTwuNyb5YKZFXYgg5ZJ6uhdrsGmFAWYveUOwJBoE4mo4i50ZtcoRysz%2FspOwi4Sp5FVLlE5ZiqgyNZK97%2FrJHEtSgQCKDVDIlSHIpwZKFfbUOIsBo5hQ4eVDM2Qkf7PlhKPtmzFo06MZ61re7VdJa6f01UiqnHSVmIZKdlEBSqbc43n24kwSHnYQIS270Wn0DYX3A3SDfGV6YFHxBp55bfGz39C4UlqDDPWSAqhQFK0MoMleGY7WDFvLjbWf0%2FKQo7KKj%2BBkU6HXFB6TWEQs%2B2P8B7qJf0R7Ah%2B7tb%2B%2F%2BR3cO2HPMad4rW%2FAVBLAwQUAAAACACbpnhRTTWYCSsBAACHAgAAEgAAAERvY18wL0RvY3VtZW50LnhtbGVRUWvDIBB%2B768Q3xc1jDFCY2kbBoUNykifh7MuDUQN1SzZv5%2FGbtr25bj77vv87s7lapId%2BBZn02pVQpJhCITi%2BtiqpoSH%2BuXhGa7oYqm%2FjkWl%2BSCFssBJlCkcVMKTtX2B0DiOmatNL3imzw3KMXmCdFZttZRaVcyyUL%2Bx6aBau6sowWSJrqGZUQvZd8yKPWsE2FUlzCHYMCNeNS9h3XcGufCB0VYr68bJ3DgQBamXrM%2FiYrU%2F%2FZiWs26jJ4oBBjnBgDziYJo2L8iV%2BG%2Fbd2Foknu3QE8JwW747Fruy%2F8ssmMz1Ldn8eYmpvPeJNl77iMf7zdHNw%2BsldKWWfejhs65QQkUZ0p5QWgt4ye%2FlBPOuVNGLFEmxPDLg7Fa1qwx1AcU6yhKONcXpItfUEsDBBQAAAAIAJumeFHs%2BF3WhAAAAMIAAAAZAAAARG9jXzAvVGFncy9DdXN0b21UYWdzLnhtbLOxr8jNUShLLSrOzM%2BzVTLUM1BSSM1Lzk%2FJzEu3VQoNcdO1ULK347LJT0uxci4tLsnPDUlML1YAasortgIK2ipllJQUWOnrl5eX6wH5xQWpyXr5Ren6RgaGZkp2qPoUQioLUj1dbJWgEm6ZOak%2B%2Bcl2cAV6QHNt9JGlIDy4AnR%2BsR0XAFBLAwQUAAAACACbpnhRS49cadwBAADpCAAAGAAAAERvY18wL1RhZ3MvQ3VzdG9tVGFnLnhtbJWW3XKCMBCF730Kh%2FsW7Y%2Bog3RsrR0vtLbaB0jDqmkxmYHg6Ns3AirKstgbk0C%2Bk032bNB92q6D%2BgbCSCjZs5q3DasOkitfyGXP%2BpoPb9rWk1dzuzCSGyU41M18GXV7luW52aMX5YPnqoXfff%2F%2BAa4%2FYVGfsiWY1ihaXuvBtc%2Feeq59hj7HOwizZsLWtNhjUSwHJt05244GpIhTIpKRSb%2Fv%2B%2BEcAkrHaZXoHNlkNBSSSS5Y0OdcxVKTkp0SyaKInZ3bDILg1F4RdqtdXOMCTof%2FCbyFBF6mkj6vSrVzX6aYkmm%2FMtkOkuwz1D4cYGbKiSLlGqVu3oNjxldCVmk0ixo58FAcJqhfUuauvLBS9jBaAf%2BtKlOHKNMTb87sRUkdqqBSD6nUS3oURTEMmKaFELvmwH0WJQ%2FiSGxgrrSx2brKq%2B3iVonJ%2BD7wNc2L1%2B0%2FgyleIsRkxMyla5oX18ZQPGJiMlLpl0tN2Q7IpHaQMsqgxG37eiRopICO2JtSfjSSCxXl%2BsZrGtakJub%2FhDGbm%2FEV0LdVB7fJARwDi%2BLQdKUeCPO7%2F96ScsinBdeozm4HMU3OI1cIIBWYA6ehuSNIHnFMBn3ETGqhdxTebCBmOYF2Lsl2Pvn28V%2BLV%2FsDUEsDBBQAAAAIAJumeFGsLhFCzwAAADIBAAAdAAAARG9jXzAvQXR0YWNocy9BdHRhY2htZW50cy54bWxljk9rwjAYxu9%2BivDemybBlhGaylAKguyi23VkMdYX0kSSYGWf3owNNtzx%2Bcfv6Va3yZGrjQmDV8ApA2K9CUf0o4LXw1A9wapfdOF0lM85a3OerM%2BJlJVPsrgKzjlfZF3P80yLThdraIhjLRhvoX8Yku2mQBgH8qInqyBEHNFr947%2BGtBYIEOIk84KCgDIOlqdy7GNzqUsmGAV55VYHgSTjZDNEsgeP78i2jRtC%2BQNE364Ypy0S%2FYHP6Czu2D6RxgtjK7%2B2%2FhWv3f%2FGalf3AFQSwMEFAAAAAgAm6Z4UcnL5HRmAQAAgwEAABYAAABEb2NfMC9SZXMvaW1hZ2VfODAuamIym%2B7lZMTLJcXFyMDAAMIMBmBKGIhToBgMGCGkGojBaI4uy8DB%2FP%2Fvf6Z%2F%2F%2F6xaOz3nPDy7%2BOU%2B0%2F2xrAXxdjZtZioyzkcq%2F25RYuh7%2BhUSd5vgbXlS%2BfZcRy5Jnbupv%2BpkoqWir2t3G%2B7co4oz15bI1ZzUJbzivTuJH0x3bpbXCLdunUbU%2FS%2BHjnRvVq1QuHkijlKJfL7ojNiL1x917mW9ZtD8EWPpRnvOPk%2FeHuqft%2BRyTo70O53d8MS5lD1RSoHXALetoRFx7z%2Fn72MM9Ja4Pjix8m%2FZx78cqhBxLhp%2Fs6ZeQLR9%2F4Klv0POl1%2FNmpdkZZcBo8kp5Vq3eGKG7FVH8pPHcr%2B6Lv%2B0ux%2Fdh%2BV9C%2BvFc2fsNgwfamI1uvV%2B1Vc9l7fWb854Hn4NDPpatadRnodU%2BXvfZPmPSz%2BnuO1g10N0%2Bpn2n%2BDJpydwqi5IemyjsaSyvb6%2F2uAAcVkCA1KBgZmYwgTAFBLAwQUAAAACACbpnhRG3d%2BjHEFAAA6CgAAIgAAAERvY18wL0F0dGFjaHMvb3JpZ2luYWxfaW52b2ljZS54bWx1Vt1PE1kUfyfxfyAk60MpzL3zPQpjZlooI0yxUHD7WIdLO7adKe1MCzytGnfVZVWiGzQhbly%2FstFIXEFZEP%2BaTilP%2Fgt7Z24%2FpohNOrnn%2B3fPuefcO3ZptVQcrKFK1bSt8SE4CoYGkWXYS6aVGx9yneURceiSPDCGNKtmmwYaxOpW9cJyeXwo7zjlCxRVr9dH0VKlNGpXcqOGRVWNPCplKTRiEguKBlAaGlwMh5DHlssX4rahxWUAx6gu4bPbgWL2EpIBAwG2BoCDRC0sDCknbVlkJQgFHoTVMNtXSq%2BV2%2B4CYZcMHFSrLopnHSTTgAbef7sQNrfv0Gxz6xXx1JWHseWRUSAeRYmTeIyPhxiqJIk814egp%2Bmb61kjb1o%2BLJ4XJMDTjMCLTKDfEwWIs6sx23IqdpFEARGGAedzzkUJ0iIrUhBGODHC4MwKwzx1bkDyZSMRThjh%2BBEODJ8vOhcZSgBAoljIS5iB5ecGAMNywzDiSylREiMRCZuwPhmB%2FpcFFOhoClLghaVoVoyIwyBQ4AALpRGGYYThcwMkmf1IffCqu4YqvVUyW0Jya3fP%2B%2Fys%2BfSgefuNd%2BNV6%2BCt92DT%2B%2FBnc%2FvuydOH3u133oP9wF%2FPpOsAh8BHQ4Ic3i5gdIW%2FLM1lGEns6RONroGytFRJo2I76PH2Dbw4efLR27%2FZONj0%2Fv3H2zjwNrYaB%2B9an3dowXvw%2BWTz7cmto9bu397OhvfyjXf%2FNet9uCmKIpZ9%2B7IBRA6OBB8Rl4vjOaEXuhOrG3zStLKWYWaLimHYruW0UZw8%2BtR6vtG6%2BbxxeBTedBvaH1vNJ%2Febj3ewDt4kPlCQBfhH04DrxfrOdU9ETk25ZhEeWeHFPCoW21KyJNX4%2BuLkxTNSh%2BM3m817v5BqfPtyp7F%2Fr7mHN32XgGztvmgcHobqE%2FLSc9qpEG4BCFhdgZNzcZXjEyGLXokI3ckbiYdLc7K1hzePS9N8utO68RiXhmUknH9WwTwaCt77l1DkIS%2F6MUDIc7gChPNdnkiQ5t7rxv422Skph%2Ff1YfPDbyTtksjghAuiCHAMP%2FeA5UNRvs99ZzhkodybFD7RXdNhQZsIFcRPiWUU3apZQ2nbwa5LgWca%2F8Boe48%2FUvIdJG1%2FLFHdVWjs4BgF%2Bfj98%2BOHv3qbT%2FomUiDyda9k1xA6pUR4vjSYXBhpv7zDbePvhx0GfRorZk2snrlZnOmQ3ZlKvoNEJVvOk2kIoxBEw1dDtDP8o4G7qD%2FKIaTZ6FnjOapKPB0N4vV8hnI3rymdioYZfTR9WoEmx8%2FMWVnHrSBZ1zRVzWWmp%2B0JYx0uJJRUKqasxFRpHf8VTVXSE7O6Uk%2FEYivqlC4tKhl9Tk0p9bhyyiadUEE8pq6nfBv1uj6ZW42tK5fVXHJRVTJppZCc1eeq9UQqE19MpWbi6kyxJDDFSuWataIJRXNlqpSbqRWrGWV1Jq6sEDtd14aRfd29Om0jtOCgq05h1qzl0DxXdpGLeam8O89W0FUqt5ZPp9NaWckZ80pdUTCY2g9wa23cao5ZmFSUuSl9YiGmpeLzhYkiv6ZJuomUErtgcO7UdG1tOqWrmpMQZnVWzBfy%2BmQ1czmn5a4l0pD%2BOakU0EpyeibjcjCmXQFuQYMLtcx6yp2RtPXJ5ES%2BYNfHST91Ux4cEtteqmrWsl3tJ0n5HFSSI62jncbhpwgZgfhCat06ahw9au79fvzx8Pjwr0X8PCG19bWDopaRYS6bRtbBz5d2E%2Fez%2FOsbZasYRAlZTtzEX%2F%2BpI3uvtsjdfpYw6MAKPj2kBUj3BbQvSblZyzGdNZk8e7qkLzurc%2Fo7bd5%2FgiEZ%2FtTpqjajLT6zYTseqP68UaeySnUegvL%2FUEsDBBQAAAAIAJumeFGSg%2B3%2BjAAAAMMAAAAcAAAARG9jXzAvQW5ub3RzL0Fubm90YXRpb25zLnhtbLOxr8jNUShLLSrOzM%2BzVTLUM1BSSM1Lzk%2FJzEu3VQoNcdO1ULK347LJT0uxcszLyy9JLAEqLFYA6sortgKK2ipllJQUWOnrl5eX6wH5xQWpyXr5Ren6RgaGZkp2YI0BiempCiDC0wVoBVTQLTMn1Sc%2F2Q4kHm%2BgjzBcD2i2jT6yEggPpBDKRHKJHRcAUEsBAgAAFAAAAAgAm6Z4UVy0SffYAAAANQEAACIAAAAAAAAAAAAAAAAAzBUAAERvY18wL0Fubm90cy9QYWdlXzAvQW5ub3RhdGlvbi54bWxQSwECAAAUAAAACACbpnhRFBopcPUAAADPAQAAEwAAAAAAAAAAAAAAAADkFgAARG9jXzAvUHVibGljUmVzLnhtbFBLAQIAABQAAAAIAJumeFFpeuV0%2FAAAAMABAAAVAAAAAAAAAAAAAAAAAAoYAABEb2NfMC9Eb2N1bWVudFJlcy54bWxQSwECAAAUAAAACACbpnhRfz8BZccGAABkGgAAHgAAAAAAAAAAAAAAAAA5GQAARG9jXzAvUGFnZXMvUGFnZV8wL0NvbnRlbnQueG1sUEsBAgAAFAAAAAgAm6Z4URS%2BTWVTBQAAejcAABwAAAAAAAAAAAAAAAAAPCAAAERvY18wL1RwbHMvVHBsXzAvQ29udGVudC54bWxQSwECAAAUAAAACACbpnhRTTWYCSsBAACHAgAAEgAAAAAAAAAAAAAAAADJJQAARG9jXzAvRG9jdW1lbnQueG1sUEsBAgAAFAAAAAgAm6Z4Uez4XdaEAAAAwgAAABkAAAAAAAAAAAAAAAAAJCcAAERvY18wL1RhZ3MvQ3VzdG9tVGFncy54bWxQSwECAAAUAAAACACbpnhRS49cadwBAADpCAAAGAAAAAAAAAAAAAAAAADfJwAARG9jXzAvVGFncy9DdXN0b21UYWcueG1sUEsBAgAAFAAAAAgAm6Z4UawuEULPAAAAMgEAAB0AAAAAAAAAAAAAAAAA8SkAAERvY18wL0F0dGFjaHMvQXR0YWNobWVudHMueG1sUEsBAgAAFAAAAAgAm6Z4UcnL5HRmAQAAgwEAABYAAAAAAAAAAAAAAAAA%2ByoAAERvY18wL1Jlcy9pbWFnZV84MC5qYjJQSwECAAAUAAAACACbpnhRG3d%2BjHEFAAA6CgAAIgAAAAAAAAAAAAAAAACVLAAARG9jXzAvQXR0YWNocy9vcmlnaW5hbF9pbnZvaWNlLnhtbFBLAQIAABQAAAAIAHmmeFFSgvYrMgIAAGcFAAAHAAAAAAAAAAAAAAAAAAAAAABPRkQueG1sUEsBAgAAFAAAAAgAm6Z4UZKD7f6MAAAAwwAAABwAAAAAAAAAAAAAAAAARjIAAERvY18wL0Fubm90cy9Bbm5vdGF0aW9ucy54bWxQSwECFAMUAAAACAB5pnhRKooN9sQDAADTCgAAIAAAAAAAAAAAAAAAtoFXAgAARG9jXzAvU2lnbnMvU2lnbl8wL1NpZ25hdHVyZS54bWxQSwECFAMUAAAACAB5pnhRXpplfV8OAABtGAAAIgAAAAAAAAAAAAAAtoFZBgAARG9jXzAvU2lnbnMvU2lnbl8wL1NpZ25lZFZhbHVlLmRhdFBLAQIUAxQAAAAIAHmmeFEqF9qknAAAANsAAAAaAAAAAAAAAAAAAAC2gfgUAABEb2NfMC9TaWducy9TaWduYXR1cmVzLnhtbFBLBQYAAAAAEAAQAHsEAAAMMwAAAAA%3D&seal_tag=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()