import "./styles.css";

import RemoteComponentWrapper from "customer_site/RemoteComponentWrapper";

// DATA EXAMPLE: uncomment these imports when this widget needs Doover data.
// import { useRemoteParams } from "customer_site/useRemoteParams";
// import { useAgentChannel } from "doover-js/react";

function WidgetTemplateContent() {
  // DATA EXAMPLE: read the current agent's latest `tag_values` aggregate.
  // Calling `useAgentChannel` performs the request, so this example remains
  // commented out to keep the base template entirely data-free.
  //
  // const { agentId } = useRemoteParams();
  // const {
  //   data,
  //   isLoading,
  //   error,
  // } = useAgentChannel<Record<string, unknown>>(agentId, "tag_values");

  return (
    <section className="widget-template">
      <p className="widget-template__eyebrow">Doover widget</p>
      <h2>Widget Template</h2>
      <p>
        Replace this static content with your widget. The commented example in
        this component shows how to load channel data when you need it.
      </p>
    </section>
  );
}

function WidgetTemplate() {
  return (
    <RemoteComponentWrapper>
      <WidgetTemplateContent />
    </RemoteComponentWrapper>
  );
}

export default WidgetTemplate;
