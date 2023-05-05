import re

search_text = '''
using CNET_V7_Domain.DataModels.ConsigneeSchema;
using CNET_V7_Entities.DataModels;
using CNET_V7_Service.Contracts;
using CNET_V7_Service.Contracts.ConsigneeSchema;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CNET_V7_Presentation.BaseControllers.ConsigneeSchema
{

    [Route("api/[controller]")]
    [ApiController]
    public class ConsigneeController : ControllerBase
    {

        private readonly IServiceManager _serviceManager;

        public ConsigneeController(IServiceManager serviceManager)
        {
            _serviceManager = serviceManager;
        }
    }
}
'''

pattern = re.compile('System.Text')

matches = pattern.finditer(search_text)

for match in matches:
    print('span: ', match.span(), ' match: ', match.match())
