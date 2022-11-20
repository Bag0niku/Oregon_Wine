import pandas as pd
import folium
from folium.plugins import MarkerCluster






def popup_html(df, i):  
    winery_name = df['name'].iloc[i] 
    winery_url = df['website'].iloc[i]
    winery_address =df['formatted_address'].iloc[i] 
    winery_phone = df['formatted_phone_number'].iloc[i]
    winery_gmaps = df['gmaps_url'].iloc[i]
    color = "Blue"
    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"

    
    html = f"""<!DOCTYPE html>
        <html>
            <body style="background-color: {right_col_color};" >
            <h4 style = "margin-bottom:10;">{winery_name}</h4>
            
            <table style="width:300px">
                <tbody>

                    <tr>
                        <td style ="padding:10px;width:150px;background-color: {left_col_color};"><span style ="color: #ffffff;">Winery URL</span>
                        </td>
                        <td style ="padding:10px;width:150px;background-color:{right_col_color};" ><a href="{winery_url}">{winery_url}</a></td>
                    </tr>
                     <tr>
                        <td style ="padding:10px;width:150px;background-color: {left_col_color};"><span style ="color: #ffffff;">Winery phone</span></td>
                        <td style ="padding:10px;width: 150px;background-color: {right_col_color};">{winery_phone}</td>
                    </tr>
                    <tr >
                        <td style ="padding:10px;width:150px;background-color: {left_col_color};"><span style = "color: #ffffff;">Address</span></td>
                        <td style ="padding:10px;width: 150px;background-color:{right_col_color};"><p>{winery_address}</p></td>
                    </tr>
                    <tr >
                        <td style ="padding:10px;width:150px;background-color: {left_col_color}"><span style ="color: #ffffff;">Google Maps location:</span></td>
                        <td style ="padding:10px;width: 150px;background-color: {right_col_color};"><a href="{winery_gmaps}">{winery_gmaps}</a></td>
                    </tr>

                </tbody>
            </table>
            </body>
        </html>
        """.format(left_col_color, right_col_color, winery_name, winery_url, winery_phone, winery_address, winery_gmaps)
    return html 




def make_markers(df):
    marker_cluster = MarkerCluster() 
    for i in range(0,len(df)):
        winery_name = df['name'].iloc[i]
        html = popup_html(df, i)
        popup = folium.Popup(folium.Html(html, script=True)) #, max_width=500
        folium.Marker([df['center_lat'].iloc[i],df['center_lon'].iloc[i]],
                    popup=popup, tooltip=winery_name,icon=folium.Icon(color='blue', prefix='fa')).add_to(marker_cluster)

    #  marker_cluster.add_to(map) 
    return marker_cluster




def make_map(df):
    map = folium.Map(location=[df.center_lat.mean(), 
                           df.center_lon.mean(),
                           ], zoom_start=8, control_scale=True)
    return map
