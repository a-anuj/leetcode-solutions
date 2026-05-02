class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_list = address.split(".")
        string = ""
        for i in range(len(address_list)):
            string+=address_list[i]
            if i!=len(address_list)-1:
                string+="[.]"
        return string