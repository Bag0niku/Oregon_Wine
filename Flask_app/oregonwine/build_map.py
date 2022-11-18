import pandas as pd
import folium
from folium.plugins import MarkerCluster






def popup_html(df, i):  
    winery_name = df['name'].iloc[i] 
    winery_url = df['website'].iloc[i]
    winery_address =df['formatted_address'].iloc[i] 
    winery_phone = df['formatted_phone_number'].iloc[i]
    color = "Blue"
    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"

    
    html = f"""<!DOCTYPE html>
        <html>
            <head>
                <h4 style = "margin-bottom:10" ; width = "200px">{winery_name}</h4>
            </head>
            <table style = "height: 126px; width: 350px;">
                <tbody>

                    <tr>
                        <td style ="background-color: {left_col_color}>
                            <span style = "color: #ffffff;">Winery URL</span>
                        </td>
                        <td style ="width: 150px;background-color:{right_col_color} >{winery_url}</td>
                    </tr>
                    <tr>
                        <td style ="background-color: left_col_color><span style = "color: #ffffff;">Address</span></td>
                        <td style ="width: 150px;background-color:{right_col_color}>{winery_address}</td>
                    </tr>
                    <tr>
                        <td style ="background-color: {left_col_color}><span style ="color: #ffffff;">Winery phone</span></td>
                        <td style ="width: 150px;background-color: {right_col_color}>{winery_phone}</td>
                    </tr>
                </tbody>
            </table>
        </html>
        """
    return html 




def make_markers(df):
    marker_cluster = MarkerCluster() 
    for i in range(0,len(df)):
        winery_name = df['name'].iloc[i]
        color = 'blue'
        html = popup_html(df, i)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)
        folium.Marker([df['center_lat'].iloc[i],df['center_lon'].iloc[i]],
                    popup=popup,icon=folium.Icon(color='blue', icon='name', prefix='fa')).add_to(marker_cluster)

    #  marker_cluster.add_to(map) 
    return marker_cluster




def make_map(df):
    map = folium.Map(location=[df.center_lat.mean(), 
                           df.center_lon.mean(),
                           ], zoom_start=8, control_scale=True)
    return map
