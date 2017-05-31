# Land Mapper

> Simple Woodland Discovery    

***  

### Progress  

- development on django branch  
- Outstanding tasks can be found as [issues](https://github.com/Ecotrust/landmapper/issues/) and aggrigated on [TODO issues](https://github.com/Ecotrust/landmapper/issues/45)
    

### Status [5.31.17]  

- pausing development
- tilestache installed on port 8080 using nginx server port 80, but not functioning as expected (see [wiki](https://github.com/Ecotrust/landmapper/wiki/Tilestache) for installing a local version of tilestache)
  - probably cause is configuration of tilestache, nginx, and uwsgi
  - both landmapper and tilestache running on different servers in virtual environment
  - use edgar.ecotrust.org as an example of running setup
  - if difficult to correct, it will be worth getting both landmapper and tilestache running on nginx (this will be prod env anyway)
  
***  
 
### Notes  
 
From marco Taxlot layer may be able use
 
 ```py
 class PlanningUnit
 ```  
 
PlanningUnit is part of OFR family but may be in marco
 
