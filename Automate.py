import os


def create_dto(model_path_dir: str, dto_path: str):
    for root, dirs, files in os.walk(model_path_dir):
        # print(f"length of files: {len(files)}")
        for file in files:
            with open(os.path.join(root, file)) as domain_file:
                filename, file_extension = os.path.splitext(file)
                dto_name = filename + 'DTO' + file_extension
                with open(os.path.join(dto_path, dto_name), 'w+') as dto_file:
                    for line in domain_file:
                        if "namespace" in line:
                            line = "namespace CNET_V7_Domain.DataModels;\n"
                        if "class" in line:
                            line = line.split('\n')[:-1][0] + 'DTO'
                        if "virtual" in line:
                            continue
                        if line.isspace():
                            continue
                        dto_file.write(line)
    print(f"All DTOS Created")


def create_irepository(model_path_dir: str, irepository_path_dir):
    schema = {
        ('Account', 'AccountMap', 'BeginingTransaction', 'ControlAccount', 'DepreciationRule', 'GSLAcctRequirement',
         'JournalDetail', 'TrialBalance'): 'Accounting',
        ('Article', 'ArticleUser', 'ConversionDefinition', 'SerialDefinition', 'Specification', 'StockBalance',
         'StockLevel', 'Value', 'ValueChangeLog'): 'Article',
        ('Activity', 'Attachment', 'BeginingBalance', 'CloudSync', 'CNETMedia', 'Country', 'Currency', 'Delegate',
         'Denomination', 'ExchangeRate', 'GSLTax', 'Holiday', 'HolidayDefinition', 'Language', 'Location', 'Movie',
         'MovieSchedule', 'ObjectState', 'Period', 'Range', 'Relation', 'ReportHistory', 'Route', 'RouteAssignment',
         'Schedule', 'ScheduleDetail', 'ScheduleHeader', 'SeasonalMessage', 'SeatArrangement', 'SeatTransaction',
         'Space', 'SpaceDirection', 'SubCountry', 'Subtitle', 'ValueFactor', 'VoucherExtension'): 'Common',
        ('Consignee', 'ConsigneeUnit', 'ConsigneeUser', 'Identification', 'LanguagePreference',
         'TransactionLimit'): 'Consignee',
        'AttendanceLog': 'Hrms',
        ('AnswerKey', 'AnswerSheet', 'BlankFill', 'Choose', 'EvaluationSheet', 'Question', 'QuestionDetail',
         'QuestionRouter', 'WriteUp'): 'Questionary',
        ('AccessMatrix', 'AcLog', 'Card', 'Functionality', 'IssuedCard', 'RoleActivity', 'User',
         'UserRoleMapper'): 'Security',
        ('ActivityDefinition', 'CNETLicense', 'Configuration', 'Device', 'DiscountFactor', 'Distribution',
         'FieldFormat', 'IDDefinition', 'IDSetting', 'MenuDesigner', 'ObjectStateDefinition',
         'OrderStationMap', 'Preference', 'PreferenceAccess', 'ProgressTaxRate', 'ReconciliationDetail',
         'ReconciliationSummary', 'RelationalState', 'Report', 'RequiredGSL', 'RequiredGSLDetail',
         'SystemConstant', 'Tax', 'TermDefinition', 'ValueFactorDefinition', 'VoucherStoreMapping'): 'Setting',
        ('ClosedRelation', 'DenominationDetail', 'LineItem', 'LineItemConversion', 'LineItemReference',
         'LineItemValueFactor', 'NonCashTransaction', 'PreferenceValueFactor', 'TaxTransaction', 'TransactionCurrency',
         'TransactionReference', 'Voucher', 'VoucherAccount', 'VoucherConsigneeList',
         'VoucherLookupList', 'VoucherTerm'): 'Transaction'
    }

    irepository_sample = '''
using CNET_V7_Entities.DataModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CNET_V7_Repository.Contracts.SchemaName
{
    public interface IEntityNameRepository : IRepository<EntityName>
    {

    }
}
    '''
    irepository_dir = 'NotFound'

    for root, dirs, files in os.walk(model_path_dir):
        filenames = [os.path.splitext(file)[0] for file in files]
        # print(filenames)
        for name in filenames:
            for key, value in schema.items():
                if name in key:
                    irepository_dir = value

            if not os.path.exists(os.path.join(irepository_path_dir, irepository_dir)):
                os.mkdir(os.path.join(irepository_path_dir, irepository_dir))

            repo_name = 'I' + name + 'Repository'
            with open(os.path.join(irepository_path_dir, irepository_dir, repo_name + '.cs'), 'w+') as file:
                # let me replace it
                this_repository = irepository_sample.replace('EntityName', name)
                this_repository = this_repository.replace('SchemaName', irepository_dir)
                file.write(this_repository)
    print(" All Irepository Files Are Created")


def create_irepository_manager(model_path_dir: str, irepository_manger_file_path: str):
    irepository_manager_header = '''
using CNET_V7_Repository.Contracts.Accounting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CNET_V7_Repository.Contracts
{
    public interface IRepositoryManager
    {
        void Save();

    '''
    irepository_manager_footer = '''
    }
}
    '''

    with open(irepository_manger_file_path, 'w+') as manager:
        for root, dirs, files in os.walk(model_path_dir):
            for file in files:
                model_name, file_extension = os.path.splitext(file)
                irepository_manager_header += f'\n\t\tI{model_name}Repository {model_name} ' + '{ get; }\n'
            irepository_manager = irepository_manager_header + irepository_manager_footer
            manager.write(irepository_manager)

    print(f"Irepository manager created")


def create_irepository_implementation(model_path_dir: str, irepository_implementation_root: str):
    schemas = {
        ('Account', 'AccountMap', 'BeginingTransaction', 'ControlAccount', 'DepreciationRule', 'GSLAcctRequirement',
         'JournalDetail', 'TrialBalance'): 'Accounting',
        ('Article', 'ArticleUser', 'ConversionDefinition', 'SerialDefinition', 'Specification', 'StockBalance',
         'StockLevel', 'Value', 'ValueChangeLog'): 'Article',
        ('Activity', 'Attachment', 'BeginingBalance', 'CloudSync', 'CNETMedia', 'Country', 'Currency', 'Delegate',
         'Denomination', 'ExchangeRate', 'GSLTax', 'Holiday', 'HolidayDefinition', 'Language', 'Location', 'Movie',
         'MovieSchedule', 'ObjectState', 'Period', 'Range', 'Relation', 'ReportHistory', 'Route', 'RouteAssignment',
         'Schedule', 'ScheduleDetail', 'ScheduleHeader', 'SeasonalMessage', 'SeatArrangement', 'SeatTransaction',
         'Space', 'SpaceDirection', 'SubCountry', 'Subtitle', 'ValueFactor', 'VoucherExtension'): 'Common',
        ('Consignee', 'ConsigneeUnit', 'ConsigneeUser', 'Identification', 'LanguagePreference',
         'TransactionLimit'): 'Consignee',
        'AttendanceLog': 'Hrms',
        ('AnswerKey', 'AnswerSheet', 'BlankFill', 'Choose', 'EvaluationSheet', 'Question', 'QuestionDetail',
         'QuestionRouter', 'WriteUp'): 'Questionary',
        ('AccessMatrix', 'AcLog', 'Card', 'Functionality', 'IssuedCard', 'RoleActivity', 'User',
         'UserRoleMapper'): 'Security',
        ('ActivityDefinition', 'CNETLicense', 'Configuration', 'Device', 'DiscountFactor', 'Distribution',
         'FieldFormat', 'IDDefinition', 'IDSetting', 'MenuDesigner', 'ObjectStateDefinition',
         'OrderStationMap', 'Preference', 'PreferenceAccess', 'ProgressTaxRate', 'ReconciliationDetail',
         'ReconciliationSummary', 'RelationalState', 'Report', 'RequiredGSL', 'RequiredGSLDetail',
         'SystemConstant', 'Tax', 'TermDefinition', 'ValueFactorDefinition', 'VoucherStoreMapping'): 'Setting',
        ('ClosedRelation', 'DenominationDetail', 'LineItem', 'LineItemConversion', 'LineItemReference',
         'LineItemValueFactor', 'NonCashTransaction', 'PreferenceValueFactor', 'TaxTransaction', 'TransactionCurrency',
         'TransactionReference', 'Voucher', 'VoucherAccount', 'VoucherConsigneeList',
         'VoucherLookupList', 'VoucherTerm'): 'Transaction'
    }

    implementation_sample = '''
using CNET_V7_Repository.Contracts;
using Microsoft.Identity.Client;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CNET_V7_Entities.DataModels;
using CNET_V7_Repository.Contracts.SCHEMA_NAME;
using Microsoft.EntityFrameworkCore;
using CNET_V7_Entities.Data;

namespace CNET_V7_Repository.Implementation.SCHEMA_NAME
{
    public class MODEL_NAMERepository : Repository<MODEL_NAME>, IMODEL_NAMERepository
    {
        public MODEL_NAMERepository(CnetV7DbContext context) : base(context)
        {
        }
    }
}

        '''
    schema = 'NotFound'

    for root, dirs, files in os.walk(model_path_dir):
        filenames = [os.path.splitext(file)[0] for file in files]
        # print(filenames)
        for name in filenames:
            for key, value in schemas.items():
                if name in key:
                    schema = value

            if not os.path.exists(os.path.join(irepository_implementation_root, schema)):
                os.mkdir(os.path.join(irepository_implementation_root, schema))

            # repo_name = 'I' + name + 'Repository'
            with open(os.path.join(irepository_implementation_root, schema, name + 'Repository.cs'), 'w+') as file:
                # let me replace it
                this_repository_imp = implementation_sample.replace('SCHEMA_NAME', schema)
                this_repository_imp = this_repository_imp.replace('MODEL_NAME', name)
                file.write(this_repository_imp)
    print(" All Irepository Implementation Files Are Created")


def create_repository_manager(model_path_dir: str, repository_manager_file_path: str):
    lazy_header = '''
using CNET_V7_Entities.Data;
using CNET_V7_Repository.Contracts;
using CNET_V7_Repository.Contracts.Accounting;
using CNET_V7_Repository.Implementation.Accounting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CNET_V7_Repository.Implementation
{
    public class RepositoryManager : IRepositoryManager
    {
        private readonly CnetV7DbContext _repositoryContext;

    '''
    print(f"Repository manager created")
