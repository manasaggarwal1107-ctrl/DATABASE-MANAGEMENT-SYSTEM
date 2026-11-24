import { useNavigate } from 'react-router-dom';
import { ShieldCheck } from 'lucide-react';
import { OriginBadge, StatusBadge } from '@/components/ui/Badge';
import { PageHeader } from '@/components/ui/PageHeader';
import { ResourceTable, originFilter } from '@/components/tables/ResourceTable';
import type { Column } from '@/components/tables/DataTable';
import { formatDate, formatInteger, formatText } from '@/lib/format';
import { endpoints } from '@/services/api/endpoints';
import type { Customer } from '@/types/api';

const columns: Column<Customer>[] = [
  { id: 'ref', header: 'Customer ref', sortKey: 'reference', cell: (c) => <span className="font-mono text-xs font-medium">{formatText(c.reference ?? c.id)}</span> },
  { id: 'status', header: 'Account status', cell: (c) => <StatusBadge status={c.status} /> },
  { id: 'orders', header: 'Orders', align: 'right', sortKey: 'orderCount', cell: (c) => formatInteger(c.orderCount) },
  { id: 'since', header: 'Customer since', cell: (c) => <span className="text-ink-muted">{formatDate(c.createdAt)}</span>, hideOnMobile: true },
  { id: 'origin', header: 'Source', cell: (c) => <OriginBadge origin={c.origin} /> },
];

export function CustomersPage() {
  const navigate = useNavigate();
  return (
    <div>
      <PageHeader
        title="Customers"
        description="Customers are identified by reference. Personal details are intentionally not displayed."
        meta={
          <span className="inline-flex items-center gap-1 text-xs text-ink-faint">
            <ShieldCheck className="h-3.5 w-3.5" aria-hidden /> Data minimised
          </span>
        }
      />
      <ResourceTable<Customer>
        endpoint={endpoints.customers.list}
        caption="Customers"
        searchPlaceholder="Search customer reference"
        columns={columns}
        rowKey={(c) => c.id}
        onRowClick={(c) => navigate(`/customers/${encodeURIComponent(c.id)}`)}
        filters={[{ key: 'status', label: 'Account status', type: 'text' }, originFilter]}
        emptyTitle="No customers"
      />
    </div>
  );
}
