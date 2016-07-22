# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::CognitiveServices
  module Models
    #
    # The list of cognitive services accounts operation response.
    #
    class CognitiveServicesAccountListResult

      include MsRestAzure

      # @return [Array<CognitiveServicesAccount>] Gets the list of Cognitive
      # Services accounts and their properties.
      attr_accessor :value


      #
      # Mapper for CognitiveServicesAccountListResult class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'CognitiveServicesAccountListResult',
          type: {
            name: 'Composite',
            class_name: 'CognitiveServicesAccountListResult',
            model_properties: {
              value: {
                required: false,
                read_only: true,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'CognitiveServicesAccountElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'CognitiveServicesAccount'
                      }
                  }
                }
              }
            }
          }
        }
      end
    end
  end
end