import json  # json package imported to create json output


def main_address(file_path='address.txt'):
    """
    This is the main method to read the address file and pass the address line to the `address_split` method
    The method takes the input as the address passed a location where the file is kept
    Prints the Json for each address line
    :return: None
    """
    global input_adr_string, json_string, street_addr, house_nr_str, address_dict
    street_addr = ''
    house_nr_str = ''
    address_dict = {}

    with open(file_path.encode("utf-8"), 'r') as file:
        for adr in file:
            street_addr, house_nr_str = address_split(adr)  # calling the function
            address_dict['street'] = street_addr.replace('\n', '').strip()
            address_dict['housenumber'] = house_nr_str.replace('\n', '').strip()

            json_string = json.dumps(address_dict, indent=4, ensure_ascii=False)

            print('printing output address json string below: ')
            print(json_string)

def address_split(adr):
    """
    Function create a split of address line into house number and street address
    :param adr: Address line as `input` in `str` format
    :return: Returns `str` of street address and house number
    """
    global house_nr, street_addr, number_pos, num_ctr, house_nr_str
    # defining and initializing parameters to control the split of address line
    num_ctr = 0
    number_pos = []
    street_addr = ' '
    house_nr_str = ' '

    if ',' in adr:
        l_addr = adr.split(',')  # split address if there is a `,` comma present in address line
    else:
        l_addr = adr.split(' ')  # split address using `space` if there is no `,` comma present in address line
    for word in l_addr:  # loop through the list containing separate elements of address line based on the split
        if l_addr[0].isdigit():  # if first word in address line is a number
            house_nr = l_addr[0]  # assign the first element to house number
            number_pos.append(0)  # add `0` in number position list
        elif word.isdigit():  # if address string contains a digit
            number_pos.append(l_addr.index(word))
            # assign the index of the element which is number to the number position list
            num_ctr += 1  # increment the number control by 1
            house_nr = word  # assign the element to house number
        elif any(map(str.isdigit, word)):  # if address string contains an alphanumeric
            number_pos.append(l_addr.index(word))
            # assign the index of the element which is number to the number position list
            num_ctr += 1  # increment the number control by 1
            house_nr = word  # assign the element to house number

    if num_ctr > 1:  # check if number control increment has been done
        end = number_pos[0] + 1  # assign the position of house number to the index position end
        street_addr = street_addr.join(l_addr[:end])  # join street address before the index position end
        house_nr_str = house_nr_str.join(l_addr[end:])  # join house number after the index position end

    elif num_ctr == 1 or l_addr[0].isdigit():
        #  if first element of address line is digit or house number is not at the end
        if l_addr[0].isdigit():  # if first element is house number
            house_nr_str = l_addr[0]  # assign first element to house number
            street_addr = street_addr.join(l_addr[1:])  # join rest of the address line as street address
        else:
            end = number_pos[0]
            if end == 0:
                end = 1
                street_addr = street_addr.join(l_addr[end:])
                house_nr_str = house_nr_str.join(l_addr[:end])
            else:
                street_addr = street_addr.join(l_addr[:end])
                house_nr_str = house_nr_str.join(l_addr[end:])
    else:
        street_addr = adr
        house_nr_str = 'none'

    if ',' in street_addr:
        street_addr = street_addr.replace(',', '')

    return street_addr, house_nr_str


if __name__ == '__main__':
    main_address('address.txt')
    # pass the input parameter as the location of address file
