import panoramix

"""
Niklas' version to decompile a file of bytecode

add a read-in function to read in the bytecode from the files
add an output function to better format the output

"""

# replace with address and code loader - load from file
address = "0x888666CA69E0f178DED6D75b5726Cee99A87D698"
code = "0x606060405236156100c45760e060020a600035046306fdde0381146100c9578063095ea7b31461012b57806318160ddd1461013e57806323b872dd1461014c578063313ce5671461016d578063366a68dc1461017e57806354fd4d50146101e457806370a08231146102475780638da5cb5b1461027157806395d89b4114610288578063a39a45b7146102eb578063a4e2d63414610374578063a9059cbb14610381578063cae9ca511461039a578063d8162db714610460578063dd62ed3e1461046e575b610002565b346100025760408051600180546020600282841615610100026000190190921691909104601f81018290048202840182019094528383526104a793908301828280156105995780601f1061056e57610100808354040283529160200191610599565b34610002576105156004356024356103f4565b346100025761052960005481565b34610002576105156004356024356044356000836105a15b60065443901190565b346100025761053b60025460ff1681565b3461000257610515600435600554600090600160a060020a0390811633909116141561026c5760068290556040805183815290517f6c04066f6ede40cc1642c211ba9d18f1a096ccc84fb8d11be28ea6c3c6f68b369181900360200190a150600161026c565b34610002576040805160048054602060026001831615610100026000190190921691909104601f81018290048202840182019094528383526104a793908301828280156105995780601f1061056e57610100808354040283529160200191610599565b3461000257610529600435600160a060020a0381166000908152600760205260409020545b919050565b3461000257610551600554600160a060020a031681565b34610002576040805160038054602060026001831615610100026000190190921691909104601f81018290048202840182019094528383526104a793908301828280156105995780601f1061056e57610100808354040283529160200191610599565b3461000257610515600435600554600090600160a060020a0390811633909116141561026c576005805473ffffffffffffffffffffffffffffffffffffffff19168317905560408051600160a060020a038416815290517f3edd90e7770f06fafde38004653b33870066c33bfc923ff6102acd601f85dfbc9181900360200190a150600161026c565b3461000257610515610164565b34610002576105156004356024356000336106cf610164565b3461000257604080516020604435600481810135601f81018490048402850184019095528484526105159481359460248035959394606494929391019181908401838280828437509496505050505050506000836107b781855b33600160a060020a03908116600081815260086020908152604080832094871680845294825280832086905580518681529051929493927f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925929181900390910190a35060015b92915050565b346100025761052960065481565b3461000257610529600435602435600160a060020a0382811660009081526008602090815260408083209385168352929052205461045a565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156105075780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b604080519115158252519081900360200190f35b60408051918252519081900360200190f35b6040805160ff9092168252519081900360200190f35b60408051600160a060020a03929092168252519081900360200190f35b820191906000526020600020905b81548152906001019060200180831161057c57829003601f168201915b505050505081565b15806105bb5750600554600160a060020a03908116908216145b156106c7578330600160a060020a031681600160a060020a03161415156106c557600160a060020a0386166000908152600760205260409020548490108015906106255750600860209081526040600081812033600160a060020a03168252909252902054849010155b80156106315750600084115b156106c057600160a060020a03858116600081815260076020908152604080832080548a0190558a851680845281842080548b90039055600883528184203390961684529482529182902080548990039055815188815291519293927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9281900390910190a3600192506106c5565b600092505b505b509392505050565b15806106e95750600554600160a060020a03908116908216145b156107b0578330600160a060020a031681600160a060020a03161415156107ae5733600160a060020a03166000908152600760205260409020548490108015906107335750600084115b156107a95733600160a060020a03908116600081815260076020908152604080832080548a90039055938916808352918490208054890190558351888152935191937fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929081900390910190a3600192506107ae565b600092505b505b5092915050565b156106c75780600160a060020a0316638f4ffcb1338630876040518560e060020a0281526004018085600160a060020a0316815260200184815260200183600160a060020a03168152602001806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f16801561085f5780820380516001836020036101000a031916815260200191505b5095505050505050600060405180830381600087803b156100025760325a03f11561000257505050600191506106c756"


panoramix.decompile(address, code)