'''
final_result_url = result_url + IDs[i] + "/year/" + years[0] + "/" + names[0]
sock = urlopen(final_result_url)
result_content = sock.read()
result_soup = BeautifulSoup(result_content, 'html.parser')
'''