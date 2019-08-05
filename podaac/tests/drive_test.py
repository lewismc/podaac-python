# Copyright 2016-2019 California Institute of Technology.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..drive import Drive
import os
from glob import glob
import unittest

class TestDrive(unittest.TestCase):
        

    def test_init_with_file(self):
        drive = Drive('podaac.ini', None, None)
        self.assertEqual(drive.USERNAME, 'podaacpy')
        self.assertEqual(drive.PASSWORD, 'hZHYQ17yuag25zivK8F')
        self.assertEqual(drive.URL, 'https://podaac-tools.jpl.nasa.gov/drive/files')

    def test_init_with_username_password_url(self):
        drive = Drive(None, 'podaac', 'ZAnTpYo', 'https://podaac-tools.jpl.nasa.gov/...')
        self.assertEqual(drive.USERNAME, 'podaac')
        self.assertEqual(drive.PASSWORD, 'ZAnTpYo')
        self.assertEqual(drive.URL, 'https://podaac-tools.jpl.nasa.gov/...')

    def test_mine_drive_urls_from_granule_search_and_download(self):
        granule_search_result = '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/terms/" xmlns:georss="http://www.georss.org/georss" xmlns:gml="http://www.opengis.net/gml" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:podaac="https://podaac.jpl.nasa.gov/opensearch/" xmlns:time="http://a9.com/-/opensearch/extensions/time/1.0/"> <title>PO.DAAC Granule Search Results</title>   <updated>2019-08-05T02:27:07.779386Z</updated>  <id>tag:podaac.jpl.nasa.gov,2019-08-05</id> <author>        <name>PO.DAAC Granule Search Service</name> </author>   <link href="https://podaac.jpl.nasa.gov/ws/search/podaac-dataset-osd.xml" rel="search" type="application/opensearchdescription+xml"/>   <link href="https://podaac.jpl.nasa.gov/ws/search/granule?datasetId=PODAAC-ASOP2-12C01&amp;startTime=2018-09-12T00:00:01Z&amp;endTime=2018-09-14T11:59:59Z&amp;bbox=-81,28,-67,40&amp;sortBy=timeAsc&amp;itemsPerPage=400&amp;format=atom&amp;pretty=true" rel="self" type="application/atom+xml"/> <link href="https://podaac.jpl.nasa.gov/ws/search/granule?datasetId=PODAAC-ASOP2-12C01&amp;startTime=2018-09-12T00:00:01Z&amp;endTime=2018-09-14T11:59:59Z&amp;bbox=-81,28,-67,40&amp;sortBy=timeAsc&amp;itemsPerPage=400&amp;format=atom&amp;pretty=true&amp;startIndex=0" rel="first" type="application/atom+xml"/>   <opensearch:totalResults>6</opensearch:totalResults>    <opensearch:startIndex>0</opensearch:startIndex>    <opensearch:itemsPerPage>400</opensearch:itemsPerPage>  <entry>     <title>ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc</title>      <updated>2018-09-13T02:00:00Z</updated>     <id>PODAAC-ASOP2-12C01:ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc</id>     <link href="https://podaac.jpl.nasa.gov/ws/search/granule?full=true&amp;granuleName=ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01" rel="enclosure" title="PO.DAAC Metadata" type="application/atom+xml"/>        <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=iso" rel="enclosure" title="ISO-19115 Metadata" type="text/xml"/>       <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=fgdc" rel="enclosure" title="FGDC Metadata" type="text/xml"/>       <link href="https://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_a/coastal_opt/2018/256/ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc.gz.html" rel="enclosure" title="OPeNDAP URL" type="text/html"/>       <link href="https://podaac-tools.jpl.nasa.gov/drive/files/allData/ascat/preview/L2/metop_a/coastal_opt/2018/256/ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc.gz" rel="enclosure" title="HTTP URL" type="application/x-netcdf"/>      <podaac:datasetId>PODAAC-ASOP2-12C01</podaac:datasetId>     <podaac:shortName>ASCATA-L2-Coastal</podaac:shortName>      <georss:box>-89.41408000000001 0.01425 89.30676000000001 359.99573000000004</georss:box>        <georss:where>          <gml:Envelope>              <gml:lowerCorner>0.01425 -89.41408000000001</gml:lowerCorner>               <gml:upperCorner>359.99573000000004 89.30676000000001</gml:upperCorner>         </gml:Envelope>     </georss:where>     <time:start>2018-09-13T02:00:00Z</time:start>       <time:end>2018-09-13T03:41:58Z</time:end>       <dc:identifier>PODAAC-ASOP2-12C01:ascat_20180913_020000_metopa_61749_eps_o_coa_2401_ovw.l2.nc</dc:identifier>       <dc:date>2018-09-13T02:00:00Z/2018-09-13T03:41:58Z</dc:date>    </entry><entry>     <title>ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc</title>      <updated>2018-09-12T00:39:00Z</updated>     <id>PODAAC-ASOP2-12C01:ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc</id>     <link href="https://podaac.jpl.nasa.gov/ws/search/granule?full=true&amp;granuleName=ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01" rel="enclosure" title="PO.DAAC Metadata" type="application/atom+xml"/>        <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=iso" rel="enclosure" title="ISO-19115 Metadata" type="text/xml"/>       <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=fgdc" rel="enclosure" title="FGDC Metadata" type="text/xml"/>       <link href="https://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_a/coastal_opt/2018/255/ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc.gz.html" rel="enclosure" title="OPeNDAP URL" type="text/html"/>       <link href="https://podaac-tools.jpl.nasa.gov/drive/files/allData/ascat/preview/L2/metop_a/coastal_opt/2018/255/ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc.gz" rel="enclosure" title="HTTP URL" type="application/x-netcdf"/>      <podaac:datasetId>PODAAC-ASOP2-12C01</podaac:datasetId>     <podaac:shortName>ASCATA-L2-Coastal</podaac:shortName>      <georss:box>-89.41189000000001 0.0015600000000000002 89.30624 359.98615</georss:box>        <georss:where>          <gml:Envelope>              <gml:lowerCorner>0.0015600000000000002 -89.41189000000001</gml:lowerCorner>             <gml:upperCorner>359.98615 89.30624</gml:upperCorner>           </gml:Envelope>     </georss:where>     <time:start>2018-09-12T00:39:00Z</time:start>       <time:end>2018-09-12T02:20:58Z</time:end>       <dc:identifier>PODAAC-ASOP2-12C01:ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc</dc:identifier>       <dc:date>2018-09-12T00:39:00Z/2018-09-12T02:20:58Z</dc:date>    <link href="https://ops-podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/preview/PODAAC-ASOP2-12C01/2018/255/ascat_20180912_003900_metopa_61734_eps_o_coa_2401_ovw.l2.nc" rel="enclosure" title="Preview Image" type="image/png"/></entry><entry>       <title>ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc</title>      <updated>2018-09-12T02:21:00Z</updated>     <id>PODAAC-ASOP2-12C01:ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc</id>     <link href="https://podaac.jpl.nasa.gov/ws/search/granule?full=true&amp;granuleName=ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01" rel="enclosure" title="PO.DAAC Metadata" type="application/atom+xml"/>        <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=iso" rel="enclosure" title="ISO-19115 Metadata" type="text/xml"/>       <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=fgdc" rel="enclosure" title="FGDC Metadata" type="text/xml"/>       <link href="https://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_a/coastal_opt/2018/255/ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc.gz.html" rel="enclosure" title="OPeNDAP URL" type="text/html"/>       <link href="https://podaac-tools.jpl.nasa.gov/drive/files/allData/ascat/preview/L2/metop_a/coastal_opt/2018/255/ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc.gz" rel="enclosure" title="HTTP URL" type="application/x-netcdf"/>      <podaac:datasetId>PODAAC-ASOP2-12C01</podaac:datasetId>     <podaac:shortName>ASCATA-L2-Coastal</podaac:shortName>      <georss:box>-89.41475000000001 0.00415 89.30636000000001 359.99426000000005</georss:box>        <georss:where>          <gml:Envelope>              <gml:lowerCorner>0.00415 -89.41475000000001</gml:lowerCorner>               <gml:upperCorner>359.99426000000005 89.30636000000001</gml:upperCorner>         </gml:Envelope>     </georss:where>     <time:start>2018-09-12T02:21:00Z</time:start>       <time:end>2018-09-12T04:02:58Z</time:end>       <dc:identifier>PODAAC-ASOP2-12C01:ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc</dc:identifier>       <dc:date>2018-09-12T02:21:00Z/2018-09-12T04:02:58Z</dc:date>    <link href="https://ops-podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/preview/PODAAC-ASOP2-12C01/2018/255/ascat_20180912_022100_metopa_61735_eps_o_coa_2401_ovw.l2.nc" rel="enclosure" title="Preview Image" type="image/png"/></entry><entry>       <title>ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc</title>      <updated>2018-09-13T13:48:00Z</updated>     <id>PODAAC-ASOP2-12C01:ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc</id>     <link href="https://podaac.jpl.nasa.gov/ws/search/granule?full=true&amp;granuleName=ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01" rel="enclosure" title="PO.DAAC Metadata" type="application/atom+xml"/>        <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=iso" rel="enclosure" title="ISO-19115 Metadata" type="text/xml"/>       <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=fgdc" rel="enclosure" title="FGDC Metadata" type="text/xml"/>       <link href="https://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_a/coastal_opt/2018/256/ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc.gz.html" rel="enclosure" title="OPeNDAP URL" type="text/html"/>       <link href="https://podaac-tools.jpl.nasa.gov/drive/files/allData/ascat/preview/L2/metop_a/coastal_opt/2018/256/ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc.gz" rel="enclosure" title="HTTP URL" type="application/x-netcdf"/>      <podaac:datasetId>PODAAC-ASOP2-12C01</podaac:datasetId>     <podaac:shortName>ASCATA-L2-Coastal</podaac:shortName>      <georss:box>-89.41489000000001 0.00041000000000000005 89.30873000000001 359.99274</georss:box>      <georss:where>          <gml:Envelope>              <gml:lowerCorner>0.00041000000000000005 -89.41489000000001</gml:lowerCorner>                <gml:upperCorner>359.99274 89.30873000000001</gml:upperCorner>          </gml:Envelope>     </georss:where>     <time:start>2018-09-13T13:48:00Z</time:start>       <time:end>2018-09-13T15:29:58Z</time:end>       <dc:identifier>PODAAC-ASOP2-12C01:ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc</dc:identifier>       <dc:date>2018-09-13T13:48:00Z/2018-09-13T15:29:58Z</dc:date>    <link href="https://ops-podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/preview/PODAAC-ASOP2-12C01/2018/256/ascat_20180913_134800_metopa_61756_eps_o_coa_2401_ovw.l2.nc" rel="enclosure" title="Preview Image" type="image/png"/></entry><entry>       <title>ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc</title>      <updated>2018-09-14T01:39:00Z</updated>     <id>PODAAC-ASOP2-12C01:ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc</id>     <link href="https://podaac.jpl.nasa.gov/ws/search/granule?full=true&amp;granuleName=ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01" rel="enclosure" title="PO.DAAC Metadata" type="application/atom+xml"/>        <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=iso" rel="enclosure" title="ISO-19115 Metadata" type="text/xml"/>       <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=fgdc" rel="enclosure" title="FGDC Metadata" type="text/xml"/>       <link href="https://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_a/coastal_opt/2018/257/ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc.gz.html" rel="enclosure" title="OPeNDAP URL" type="text/html"/>       <link href="https://podaac-tools.jpl.nasa.gov/drive/files/allData/ascat/preview/L2/metop_a/coastal_opt/2018/257/ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc.gz" rel="enclosure" title="HTTP URL" type="application/x-netcdf"/>      <podaac:datasetId>PODAAC-ASOP2-12C01</podaac:datasetId>     <podaac:shortName>ASCATA-L2-Coastal</podaac:shortName>      <georss:box>-89.41182 0.0064600000000000005 89.3054 359.9968</georss:box>       <georss:where>          <gml:Envelope>              <gml:lowerCorner>0.0064600000000000005 -89.41182</gml:lowerCorner>              <gml:upperCorner>359.9968 89.3054</gml:upperCorner>         </gml:Envelope>     </georss:where>     <time:start>2018-09-14T01:39:00Z</time:start>       <time:end>2018-09-14T03:20:58Z</time:end>       <dc:identifier>PODAAC-ASOP2-12C01:ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc</dc:identifier>       <dc:date>2018-09-14T01:39:00Z/2018-09-14T03:20:58Z</dc:date>    <link href="https://ops-podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/preview/PODAAC-ASOP2-12C01/2018/257/ascat_20180914_013900_metopa_61763_eps_o_coa_2401_ovw.l2.nc" rel="enclosure" title="Preview Image" type="image/png"/></entry><entry>       <title>ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc</title>      <updated>2018-09-12T14:09:00Z</updated>     <id>PODAAC-ASOP2-12C01:ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc</id>     <link href="https://podaac.jpl.nasa.gov/ws/search/granule?full=true&amp;granuleName=ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01" rel="enclosure" title="PO.DAAC Metadata" type="application/atom+xml"/>        <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=iso" rel="enclosure" title="ISO-19115 Metadata" type="text/xml"/>       <link href="https://podaac.jpl.nasa.gov/ws/metadata/granule?granuleName=ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc&amp;datasetId=PODAAC-ASOP2-12C01&amp;format=fgdc" rel="enclosure" title="FGDC Metadata" type="text/xml"/>       <link href="https://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_a/coastal_opt/2018/255/ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc.gz.html" rel="enclosure" title="OPeNDAP URL" type="text/html"/>       <link href="https://podaac-tools.jpl.nasa.gov/drive/files/allData/ascat/preview/L2/metop_a/coastal_opt/2018/255/ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc.gz" rel="enclosure" title="HTTP URL" type="application/x-netcdf"/>      <podaac:datasetId>PODAAC-ASOP2-12C01</podaac:datasetId>     <podaac:shortName>ASCATA-L2-Coastal</podaac:shortName>      <georss:box>-89.41476 0.008650000000000001 89.30516 359.99994000000004</georss:box>     <georss:where>          <gml:Envelope>              <gml:lowerCorner>0.008650000000000001 -89.41476</gml:lowerCorner>               <gml:upperCorner>359.99994000000004 89.30516</gml:upperCorner>          </gml:Envelope>     </georss:where>     <time:start>2018-09-12T14:09:00Z</time:start>       <time:end>2018-09-12T15:50:58Z</time:end>       <dc:identifier>PODAAC-ASOP2-12C01:ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc</dc:identifier>       <dc:date>2018-09-12T14:09:00Z/2018-09-12T15:50:58Z</dc:date>    <link href="https://ops-podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/preview/PODAAC-ASOP2-12C01/2018/255/ascat_20180912_140900_metopa_61742_eps_o_coa_2401_ovw.l2.nc" rel="enclosure" title="Preview Image" type="image/png"/></entry></feed>'
        drive = Drive('podaac.ini', None, None)
        drive_urls = drive.mine_drive_urls_from_granule_search(granule_search_response=(str(granule_search_result)))
        self.assertEqual(6, len(drive_urls))
        drive.download_granules(granule_collection=drive_urls, path='./podaac/tests/')
        self.assertEqual(6, len([y for x in os.walk('./podaac/tests/allData') for y in glob(os.path.join(x[0], '*.nc'))]))
