# earthquakes_central_asia
This code fetches earthquake data from the FDSN IRIS web service for a specific region and timeframe, then processes and presents it in two different ways:

1. CSV file:
The code retrieves earthquakes within a 10 km radius of Misol (latitude 41.0, longitude 64.0) for the past 30 days, with no minimum magnitude restriction.
It extracts information like event time, location, depth, and magnitude types for each earthquake and stores them in a pandas DataFrame.
Finally, the DataFrame is saved as a CSV file named "orta_osiyo_zilzila_ma'lumotlar.csv" for easy access and analysis.

2. QuakeML file:
The code repeats the data retrieval with the same parameters.
Instead of converting the data to a DataFrame, it directly writes the event objects to an XML file named "orta_osiyo_zilzilalar_quakeml.xml" in the QuakeML format.
This format is commonly used for sharing earthquake data and is suitable for further processing and analysis with specialized tools.
In summary, this code serves as a powerful tool for downloading and managing earthquake data for a specific region, offering both easy-to-read CSV reports and machine-readable QuakeML files for further analysis.

Main dependencies:
obspy: This is the fundamental library for seismic data processing and analysis. It provides functionalities for accessing data from FDSN web services, handling event information, and manipulating waveforms.
pandas: This data manipulation library enables you to efficiently organize and analyze the retrieved earthquake data into a table format (DataFrame) for further exploration and visualization.
datetime: This library is used for handling and manipulating date and time information, particularly for setting the search timeframe for past earthquakes.
