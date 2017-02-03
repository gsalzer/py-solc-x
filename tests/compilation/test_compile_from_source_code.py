from solc import (
    get_solc_version,
    get_solc_version_string,
    compile_source,
)


def test_source_code_compilation(SUPPORTED_SOLC_VERSIONS):
    solc_version_string = get_solc_version_string()

    solc_version = get_solc_version()

    if solc_version in SUPPORTED_SOLC_VERSIONS:
        SOURCE = "pragma solidity ^0.4.0;\ncontract Foo { function Foo() {} function return13() returns (uint) { return 13; } }"
    else:
        raise AssertionError("Unsupported compiler version: {0}".format(solc_version))


    output = compile_source(SOURCE, optimize=True)
    assert output
    assert 'Foo' in output

    foo_contract_data = output['Foo']
    assert 'bin' in foo_contract_data
    assert 'bin-runtime' in foo_contract_data
