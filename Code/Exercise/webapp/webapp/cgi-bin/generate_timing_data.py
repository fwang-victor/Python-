import cgi
import athletemodel
import yate
import cgitb

#cgitb.enable()
athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header('coach kelly timing data'))
print(yate.header('athlete:' + athlete_name + 'Dob:' + athletes[athlete_name].dob + '.'))
print(yate.para('the top times for this athlete are:'))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({'Home':'/index.html',
                           'select another athlete':'generate_list.py'}))