# custom filtering extensions

'''
These methods are applied by the following procedure:
    define the method with an argument for the incoming data
    add any required code to manipulate the data
    return the resultant data
    attach the new method
'''

# for custom processing before standard processing
#def custom_pre_process(data):
#	return(f'F#<_hal[plasmac.cut-feed-rate]>\n\n{data}')
#self.custom_pre_process = custom_pre_process


# for custom parsing before standard parsing
# Suits Hypertherm Nestmaster
incSet = False
def custom_pre_parse(data):
    global incSet
    if data[:3] in ['G20', 'G21']:
        return(f'{data}\nG90')
    elif data[:3] == 'M07':
        return(f'\nF#<_hal[plasmac.cut-feed-rate]>\nM3 $0')
    elif data[:3] == 'M08':
        return(f'M5 $0\n')
    elif data[:3] == 'M30':
        return(f'G90\n{data}')
    elif data[:3] == 'G00' and not incSet:
        incSet = True
        return(f'G91\n{data}')
    elif data[:3] == 'G91':
        return None
    return(data)
self.custom_pre_parse = custom_pre_parse

# for custom parsing after standard parsing
#def custom_post_parse(data):
#	if data[:3] == 'G64':
#		return(f'G91 G64 P0.1\n\n')	
#self.custom_post_parse = custom_post_parse

# override the original parse_code procedure

